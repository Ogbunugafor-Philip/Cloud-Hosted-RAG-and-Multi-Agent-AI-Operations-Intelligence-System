import os
import sys
import time

# Fix path logic
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from router import get_router_agent
from task_agent import run_task_agent
from rag_pipeline import run_rag_pipeline
from memory import get_session_memory
from logger import log_routing_event

def run_ops_intelligence(user_query, session_id="default_user", collection="test_collection"):
    """
    Final Stable Multi-Agent Pipeline
    """
    start_time = time.time()
    
    # 1. Load Session Memory (Using our SimpleMemory class)
    memory = get_session_memory(session_id)
    # FIX: Use the correct method we defined in memory.py
    history_context = memory.get_history_string()
    
    # 2. Routing Decision
    router = get_router_agent()
    decision = router.invoke({"question": f"Context: {history_context}\nQuestion: {user_query}"})
    choice = decision.datasource
    
    # 3. Execution Path
    try:
        if choice == "rag_pipeline":
            response_data = run_rag_pipeline(user_query, collection=collection)
            agent_label = "RAG Specialist"
        else:
            response_data = run_task_agent(user_query, collection=collection)
            agent_label = "Task Specialist"
        status = "success"
    except Exception as e:
        response_data = {"answer": f"Error: {str(e)}", "metadata": {}}
        agent_label = "Error Handler"
        status = "failed"
    
    # 4. Save to Memory (Using our SimpleMemory class)
    memory.save_context(user_query, response_data["answer"])
    
    # 5. Log Performance
    latency = round(time.time() - start_time, 3)
    log_routing_event(user_query, choice, agent_label, latency, status)
    
    return {
        "status": status,
        "agent": agent_label,
        "answer": response_data["answer"],
        "metadata": {
            "latency": latency,
            "route": choice,
            "session_id": session_id
        }
    }

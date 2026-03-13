import os
import sys
import time
from langchain_cerebras import ChatCerebras
from langchain_core.prompts import ChatPromptTemplate

# Ensure the scripts directory is in the path so we can find rag_pipeline
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rag_pipeline import run_rag_pipeline

# 1. Initialize the Task Specialist LLM
llm = ChatCerebras(
    model="llama3.1-8b",
    cerebras_api_key=os.environ.get("CEREBRAS_API_KEY"),
    temperature=0.2 
)

# 2. Define the Task Specialist Prompt
TASK_SYSTEM_PROMPT = """
You are a Senior Operations Analyst Agent. Your role is to perform complex tasks including:
- Summarizing multiple documents or events.
- Comparing different sets of information.
- Identifying trends, risks, or action items across sources.

INSTRUCTIONS:
1. Synthesize the provided context into a professional, structured response.
2. Use bullet points for readability.
3. If the context is insufficient, state exactly what is missing.
"""

def run_task_agent(user_query, collection="test_collection"):
    start_time = time.time()
    
    # Step A: Gather context using our existing RAG pipeline
    raw_context_data = run_rag_pipeline(user_query, collection=collection)
    context_text = raw_context_data.get("answer", "No context available.")
    
    # Step B: Perform Synthesis
    prompt = ChatPromptTemplate.from_messages([
        ("system", TASK_SYSTEM_PROMPT),
        ("human", "Task: {query}\n\nSupporting Evidence: {evidence}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({
        "query": user_query,
        "evidence": context_text
    })
    
    latency = round(time.time() - start_time, 3)
    
    return {
        "status": "success",
        "agent": "task_agent",
        "answer": response.content,
        "metadata": {
            "latency_seconds": latency,
            "source_count": raw_context_data.get("metadata", {}).get("chunks_used", 0)
        }
    }

if __name__ == "__main__":
    print("\n--- Testing Task Agent Synthesis (Fixed Imports) ---")
    test_task = "Summarize the key takeaways from the provided test content."
    result = run_task_agent(test_task)
    print(f"Agent Response:\n{result['answer']}")
    print(f"Latency: {result['metadata']['latency_seconds']}s")

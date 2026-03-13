import os
from typing import Literal
from pydantic import BaseModel, Field
from langchain_cerebras import ChatCerebras
from langchain_core.prompts import ChatPromptTemplate

# 1. Structured Output Schema
class RouteQuery(BaseModel):
    """Route a user query to the most appropriate AI handler."""
    datasource: Literal["rag_pipeline", "task_agent"] = Field(
        ...,
        description="Select 'rag_pipeline' for factual questions and 'task_agent' for complex analysis/summaries.",
    )

# 2. Router Initialization
def get_router_agent():
    """
    Returns a configured Router Agent that classifies user intent.
    """
    llm = ChatCerebras(
        model="llama3.1-8b",
        cerebras_api_key=os.environ.get("CEREBRAS_API_KEY")
    )
    
    # We use a strict system prompt to ensure accurate routing
    system_prompt = (
        "You are an Operations Intelligence Router. "
        "Your job is to look at a user query and decide the best tool to handle it.\n\n"
        "RULES:\n"
        "1. Use 'rag_pipeline' if the user asks for a specific fact, policy, or detail from a document.\n"
        "2. Use 'task_agent' if the user wants a summary of multiple things, a comparison, "
        "or a multi-step project (e.g., 'Analyze the trends in these reports').\n\n"
        "Decision Priority: If it's a direct question, choose 'rag_pipeline'."
    )

    structured_router = llm.with_structured_output(RouteQuery)
    
    route_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{question}"),
    ])
    
    return route_prompt | structured_router

if __name__ == "__main__":
    # Test 5.2: Verification of the Router Specialist
    router = get_router_agent()
    
    # Check a Fact-based query
    res_rag = router.invoke({"question": "What is the reimbursement limit for travel?"})
    print(f"Fact Query -> {res_rag.datasource}")
    
    # Check a Synthesis-based query
    res_task = router.invoke({"question": "Write a 3-paragraph executive summary of the last 5 project updates."})
    print(f"Task Query -> {res_task.datasource}")

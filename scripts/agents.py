import os
from typing import Literal
from pydantic import BaseModel, Field
from langchain_cerebras import ChatCerebras
from langchain_core.prompts import ChatPromptTemplate

class RouteQuery(BaseModel):
    """Route a user query to the most appropriate helper."""
    datasource: Literal["rag_pipeline", "task_agent"] = Field(
        ...,
        description="Given a user question choose to route it to the RAG pipeline or a specialized Task Agent.",
    )

llm = ChatCerebras(
    model="llama3.1-8b",
    cerebras_api_key=os.environ.get("CEREBRAS_API_KEY")
)

# REFINED PROMPT: Explicitly tells the AI that basic questions MUST go to RAG.
system_prompt = """You are a routing specialist.
1. Route to 'rag_pipeline' if the user asks a direct question about a policy, a specific fact, or 'how-to' information found in a single document.
2. Route to 'task_agent' ONLY if the request requires summarizing multiple files, comparing different reports, or performing complex analysis.

If it is a simple question, you MUST use 'rag_pipeline'."""

def get_router():
    structured_llm_router = llm.with_structured_output(RouteQuery)
    route_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{question}"),
    ])
    return route_prompt | structured_llm_router

if __name__ == "__main__":
    router = get_router()
    
    # Test 1: Should be RAG
    test_1 = router.invoke({"question": "What is the company policy on remote work?"})
    print(f"Simple Query Route: {test_1.datasource}")
    
    # Test 2: Should be Task Agent
    test_2 = router.invoke({"question": "Compare the 2024 budget report with the 2025 projections."})
    print(f"Complex Query Route: {test_2.datasource}")

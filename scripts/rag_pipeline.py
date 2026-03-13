import os
import time
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from langchain_cerebras import ChatCerebras
from langchain_core.prompts import ChatPromptTemplate

# Initialize core components
model = SentenceTransformer('all-MiniLM-L6-v2')
client = QdrantClient(host="localhost", port=6333)
llm = ChatCerebras(
    model="llama3.1-8b",
    cerebras_api_key=os.environ.get("CEREBRAS_API_KEY")
)

RAG_PROMPT_TEMPLATE = """
You are a specialized AI Operations Assistant. Use the provided context to answer the user question.

Rules:
1. Only use the provided context to answer.
2. If the answer is not in the context, say "I don't have enough information."
3. Cite the source for each fact (e.g., "Source: manual.pdf").

Context:
{context}

Question:
{question}
"""

def run_rag_pipeline(user_query, collection="test_collection"):
    start_time = time.time()
    if not user_query.strip():
        return {"error": "Empty query"}
    
    query_vector = model.encode(user_query).tolist()
    
    search_results = client.query_points(
        collection_name=collection,
        query=query_vector,
        limit=3,
        with_payload=True
    ).points
    
    relevant_hits = [hit for hit in search_results if hit.score >= 0.3]
    
    # 1. Capture the raw text for RAGAS
    retrieved_texts = [hit.payload.get("text", "") for hit in relevant_hits]
    
    # 2. Assemble context for the LLM
    context_parts = []
    sources_list = []
    for i, hit in enumerate(relevant_hits):
        text = hit.payload.get("text", "")
        source = hit.payload.get("filename", "Unknown Source")
        context_parts.append(f"[{i+1}] {text} (Source: {source})")
        if source not in sources_list:
            sources_list.append(source)
    
    context_text = "\n\n".join(context_parts) if relevant_hits else "No context found."
    
    # 3. Generate Answer
    prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)
    chain = prompt | llm
    response = chain.invoke({"context": context_text, "question": user_query})
    
    latency = round(time.time() - start_time, 3)
    
    return {
        "answer": response.content,
        "metadata": {
            "latency_seconds": latency,
            "chunks_used": len(relevant_hits),
            "retrieved_contexts": retrieved_texts,  # CRITICAL FOR RAGAS
            "citations": sources_list
        }
    }

import time
import pandas as pd
import os
import sys

# Ensure we can import the pipeline
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.rag_pipeline import run_rag_pipeline

def run_latency_benchmark():
    test_queries = [
        "What is the stipend?",
        "Tell me about Wednesdays.",
        "How do I travel?",
        "Non-existent topic test."
    ]
    
    stats = []
    print("--- Running Latency Benchmarks ---")
    
    for query in test_queries:
        start = time.time()
        response = run_rag_pipeline(query)
        end = time.time()
        
        duration = round(end - start, 3)
        print(f"Query: {query} | Latency: {duration}s")
        
        stats.append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "query": query,
            "latency": duration,
            "chunks_retrieved": response.get("metadata", {}).get("chunks_used", 0)
        })
    
    df = pd.DataFrame(stats)
    log_file = "logs/latency_benchmarks.csv"
    
    if not os.path.exists("logs"):
        os.makedirs("logs")
        
    df.to_csv(log_file, mode='a', header=not os.path.exists(log_file), index=False)
    print(f"\nBenchmark complete. Average Latency: {df['latency'].mean():.3f}s")

if __name__ == "__main__":
    run_latency_benchmark()

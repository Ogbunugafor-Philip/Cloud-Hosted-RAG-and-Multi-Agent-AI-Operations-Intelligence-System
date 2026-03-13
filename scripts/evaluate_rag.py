import pandas as pd
import os

# 7.1: Define the Ground Truth Dataset
# In a production environment, this would be a CSV or JSON file 
# compiled by subject matter experts.
test_data = [
    {
        "question": "What is the equipment stipend amount?",
        "ground_truth": "The company provides a $500 equipment stipend for remote work setup.",
        "context": "Employees are eligible for a $500 one-time equipment stipend to set up their home office. (Source: policy.pdf)"
    },
    {
        "question": "Does the policy mention Wednesdays?",
        "ground_truth": "Yes, Wednesdays are designated as 'Deep Work' days with no internal meetings.",
        "context": "To increase productivity, Wednesdays are designated as Deep Work days. No internal meetings should be scheduled. (Source: operations_manual.docx)"
    },
    {
        "question": "What is the reimbursement limit for travel meals?",
        "ground_truth": "The daily limit for travel meal reimbursement is $75.",
        "context": "Travel expenses include a daily meal allowance capped at $75 per day. (Source: travel_policy.txt)"
    }
]

def prepare_dataset():
    df = pd.DataFrame(test_data)
    if not os.path.exists("data/eval"):
        os.makedirs("data/eval")
    df.to_csv("data/eval/ground_truth.csv", index=False)
    print(f"Created evaluation dataset with {len(df)} samples at data/eval/ground_truth.csv")
    return df

if __name__ == "__main__":
    prepare_dataset()

import sys
import time
# Ensure we can import the RAG pipeline
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.rag_pipeline import run_rag_pipeline

def run_evaluation_run():
    # Load the ground truth we just created
    df = pd.read_csv("data/eval/ground_truth.csv")
    
    results = []
    
    print("Starting RAG Evaluation Run...")
    for index, row in df.iterrows():
        question = row['question']
        print(f"Testing Question {index + 1}: {question}")
        
        # Run the actual RAG pipeline
        # Note: Ensure you have 'test_collection' populated in Qdrant!
        response = run_rag_pipeline(question, collection="test_collection")
        
        # Collect the components RAGAS needs
        results.append({
            "question": question,
            "answer": response["answer"],
            "contexts": [hit.payload.get("text", "") for hit in (response.get("metadata", {}).get("raw_hits", []))], # We'll ensure raw_hits are passed
            "ground_truth": row['ground_truth'],
            "latency": response["metadata"]["latency_seconds"]
        })
        
    # Save the results for RAGAS processing
    results_df = pd.DataFrame(results)
    results_df.to_csv("data/eval/results_for_ragas.csv", index=False)
    print("Evaluation run complete. Results saved to data/eval/results_for_ragas.csv")

if __name__ == "__main__":
    # If the file is run directly, it will prepare data and then run the test
    prepare_dataset()
    run_evaluation_run()

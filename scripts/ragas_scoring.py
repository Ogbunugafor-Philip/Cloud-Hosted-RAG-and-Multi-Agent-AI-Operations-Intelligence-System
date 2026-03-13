import pandas as pd
import os
import ast
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from ragas.llms import llm_factory
from ragas.embeddings.base import LangchainEmbeddingsWrapper
from langchain_community.embeddings import HuggingFaceEmbeddings
from openai import OpenAI
from datasets import Dataset

# 1. Setup Cerebras Client for LLM
cerebras_client = OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=os.environ.get("CEREBRAS_API_KEY")
)
ragas_llm = llm_factory(model="llama3.1-8b", client=cerebras_client)

# 2. Fix Embeddings: Wrap LangChain HF Embeddings for Ragas
# This explicitly provides the 'embed_query' method Ragas is looking for
hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
ragas_embeddings = LangchainEmbeddingsWrapper(hf_embeddings)

def run_evaluation_metrics():
    input_file = "data/eval/results_for_ragas.csv"
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return

    df = pd.read_csv(input_file)
    df['contexts'] = df['contexts'].apply(ast.literal_eval)
    eval_dataset = Dataset.from_pandas(df)

    print("\n--- Starting RAGAS Mathematical Evaluation (v0.4 Stable Wrapper) ---")
    
    # 3. Assign components to metrics
    faithfulness.llm = ragas_llm
    answer_relevancy.llm = ragas_llm
    answer_relevancy.embeddings = ragas_embeddings
    context_precision.llm = ragas_llm

    # 4. Perform the Evaluation
    result = evaluate(
        eval_dataset,
        metrics=[faithfulness, answer_relevancy, context_precision]
    )

    # 5. Save and Display Results
    final_scores_df = result.to_pandas()
    final_scores_df.to_csv("data/eval/final_ragas_report.csv", index=False)
    
    print("\n--- EVALUATION SUMMARY ---")
    print(f"Mean Faithfulness: {final_scores_df['faithfulness'].mean():.4f}")
    print(f"Mean Answer Relevancy: {final_scores_df['answer_relevancy'].mean():.4f}")
    print(f"Mean Context Precision: {final_scores_df['context_precision'].mean():.4f}")
    print("\nFull report saved to data/eval/final_ragas_report.csv")

if __name__ == "__main__":
    run_evaluation_metrics()

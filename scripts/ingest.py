import os
from pypdf import PdfReader
from docx import Document

def extract_text(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    text = ""
    
    if ext == ".pdf":
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif ext == ".docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        print(f"Unsupported file type: {ext}")
    
    return text

# Quick test check
if __name__ == "__main__":
    print("Extractor ready.")

import re

def clean_text(text):
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters but keep punctuation
    text = re.sub(r'[^\x00-\x7f]', r'', text)
    return text.strip()

# Test the cleaner
sample = "This is a   test\nwith weird   spacing."
print(f"Cleaned: {clean_text(sample)}")

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    return chunks

# Test chunking
long_text = "Knowledge is power. " * 50
test_chunks = chunk_text(long_text)
print(f"Created {len(test_chunks)} chunks.")

from datetime import datetime

def create_metadata(file_name, category="General"):
    return {
        "filename": file_name,
        "category": category,
        "ingested_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Test metadata
print(f"Metadata sample: {create_metadata('policy.pdf', 'HR')}")

from sentence_transformers import SentenceTransformer

# Load a small, fast model
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text_chunks):
    # This turns the list of text into a list of number vectors
    embeddings = model.encode(text_chunks)
    return embeddings

# Test embedding
sample_emb = generate_embeddings(["Test chunk"])
print(f"Embedding generated. Shape: {sample_emb.shape}")

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

# Connect to your Qdrant service
client = QdrantClient(host="localhost", port=6333)

def store_in_qdrant(collection_name, chunks, embeddings, metadata):
    # Create the collection if it doesn't exist
    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )
    
    # Prepare data for upload
    points = []
    for i, (chunk, vector) in enumerate(zip(chunks, embeddings)):
        points.append(PointStruct(
            id=str(uuid.uuid4()),
            vector=vector.tolist(),
            payload={"text": chunk, **metadata}
        ))
    
    # Upload to Qdrant
    client.upsert(collection_name=collection_name, points=points)
    print(f"Successfully stored {len(points)} points in '{collection_name}'")

# Final Test Run
store_in_qdrant("test_collection", ["Test chunk content"], sample_emb, {"test": "data"})

def process_file(file_path, collection_name, category="General"):
    print(f"Starting ingestion for: {file_path}")
    raw_text = extract_text(file_path)
    clean_txt = clean_text(raw_text)
    chunks = chunk_text(clean_txt)
    metadata = create_metadata(os.path.basename(file_path), category)
    embeddings = generate_embeddings(chunks)
    store_in_qdrant(collection_name, chunks, embeddings, metadata)
    print(f"Finished processing {file_path}")

# To use this: process_file('path/to/your/file.pdf', 'ai_ops_docs')

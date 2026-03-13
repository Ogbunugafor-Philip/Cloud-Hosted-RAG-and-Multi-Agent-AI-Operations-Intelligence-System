# Cloud-Hosted-RAG-and-Multi-Agent-AI-Operations-Intelligence-System

<img width="974" height="650" alt="Image" src="https://github.com/user-attachments/assets/bddcbb28-835c-4047-81f6-957f58775002" />


## Introduction
Organizations generate large amounts of internal information every day through reports, policies, manuals, emails, and operational documents. Although these documents contain valuable knowledge, they are often stored in different systems and formats, which makes it difficult for employees to quickly find the information they need. Staff members frequently spend time searching through files, asking colleagues questions, or manually reviewing documents before they can make decisions or complete tasks.
The Cloud Hosted RAG and Multi Agent AI Operations Intelligence System is designed to solve this problem by creating an intelligent platform that can retrieve and use organizational knowledge automatically. The system uses Retrieval Augmented Generation to search a vector database for relevant information and produce accurate responses grounded in real documents. It also introduces AI agents that can assist with operational tasks such as answering questions, summarizing information, and supporting decision making. The system is deployed in the cloud and accessed through API services so it can be integrated with other applications and automation workflows.

## Statement of Problem
Many organizations struggle to effectively use the knowledge stored in their internal documents and operational systems. Important information is often scattered across different files, databases, and communication platforms, which makes it difficult to locate when it is needed. Employees may spend significant time searching for answers, reviewing large volumes of documents, and interpreting information before taking action. This situation leads to slow decision making, inconsistent knowledge sharing, reduced productivity, and operational inefficiencies across teams.

## Project Objectives

i.	To develop a cloud hosted Retrieval Augmented Generation system that retrieves relevant knowledge from internal documents using embeddings and a vector database.

ii.	To design and implement multi agent AI workflows that can perform tasks such as answering operational questions, summarizing documents, and assisting decision making.

iii.	To build API endpoints that allow the AI system to be accessed and integrated with external applications, automation platforms, and enterprise tools.

iv.	To implement evaluation and monitoring mechanisms that measure retrieval accuracy, response quality, and system performance to ensure reliable AI outputs.

## Tech Stack for Cloud Hosted RAG and Multi Agent AI Operations Intelligence System

Core Programming Language: Python: Main language used to build the RAG pipeline, agent logic, evaluation scripts, and API services.

LLM Reasoning Engine: Cerebras API: Generates answers, summaries, and agent outputs based on retrieved context.

Embeddings and Vector Search: Sentence Transformers (Embeddings): Converts documents and queries into vector representations for semantic search. Qdrant (Vector Database): Stores embeddings and enables fast similarity search for retrieval.

RAG and Agent Orchestration: LangChain or LlamaIndex: Manages document chunking, retrieval pipelines, tool usage, memory, and multi agent workflows.

API and Backend Service: FastAPI: Exposes the system as API endpoints for ingestion, querying, and agent task execution.

Data Processing: Pandas: Cleans, structures, and prepares document data for ingestion and evaluation.

Evaluation and Testing: RAGAS: Evaluates RAG quality using metrics like faithfulness, answer relevance, and context precision. Latency Benchmarks (Python timers): Measures response speed and performance for production readiness.

Monitoring and Dashboard: Streamlit: Provides a live dashboard showing usage, retrieval performance, latency, and evaluation results.

Deployment and Operations: Linux VPS (Cloud Hosting): Runs the API and dashboard online. systemd: Keeps FastAPI and Streamlit running 24/7 with auto restart.

Git: Version control for the project code.

## Project Workflow
i. Document Ingestion: An admin uploads documents such as policies, SOPs, reports, FAQs, or internal notes into the system through an upload page or an API endpoint.

ii. Text Extraction and Cleaning: The system extracts the text, removes noise (extra spaces, repeated headers, broken lines), and prepares the content for processing.

iii. Chunking and Metadata Tagging: The text is split into small meaningful chunks. Each chunk is saved with metadata such as document name, department, date, and category.

iv. Embedding Generation: Each chunk is converted into embeddings using a free embedding model from sentence transformers.

v. Vector Storage in Qdrant: All embeddings and metadata are stored inside Qdrant so the system can search by meaning, not just keyword.

vi. User Query or Task Request: A user sends a question or task request through the API, dashboard, or an automation tool like n8n.

vii. Retrieval Step (RAG Retrieval): The system converts the user query into an embedding, searches Qdrant, and retrieves the top relevant chunks based on similarity.

viii. Answer Generation with Cerebras: The retrieved chunks are passed to the LLM (Cerebras) as context. The model generates an answer that is grounded in the retrieved documents and returns citations.

ix. Multi Agent Execution (When needed): If the request is a complex task, a Router Agent determines the appropriate handler and directs it to the Task Agent, which retrieves evidence and generates a structured response 
before returning the result

x. Evaluation and Monitoring: Every response is logged. The system measures retrieval quality, response faithfulness, and latency. Results are stored for reporting.

xi. Dashboard Update: The Streamlit dashboard updates in real time to show queries handled, response categories, latency trends, and quality evaluation scores.

xii. Cloud Deployment and Always on Execution: FastAPI runs as a service for API access and Streamlit runs for monitoring. Both services stay online using systemd for auto restart and continuous operation.

 
## Implementation Phases
### Phase 1: Environment Setup
Phase 1 focuses on preparing the cloud workspace so the AI has a clean and isolated home. We will log in remotely and create a dedicated folder for our files. Then we will set up a Virtual Environment. This acts like a private bubble to keep the project tools like Python and FastAPI from getting mixed up with anything else on the system.

#### 1.1	SSH into VPS and create project folder structure
•	SSH into your cloud vps and run the below commands to create our project folders;
```
mkdir ai_ops_system
cd ai_ops_system
mkdir data docs scripts logs
```
<img width="872" height="286" alt="Image" src="https://github.com/user-attachments/assets/5894aee0-55d5-43a5-a439-d259ec333e60" />

#### 1.2	Create and activate Python virtual environment
•	Now we create your isolated Python workspace. Run these two commands to build and enter your virtual environment. Run;
```
python3 -m venv venv
source venv/bin/activate
```
 <img width="781" height="191" alt="Image" src="https://github.com/user-attachments/assets/160390fa-d39d-403a-a661-c9a668ff5b57" />

#### 1.3	Create requirements.txt with all dependencies
•	Create a file named requirements.txt in your main folder. Use this command to add all the core libraries we need for the RAG system and AI agents. Paste the below inside it
```
fastapi
uvicorn
qdrant-client
sentence-transformers
langchain
langchain-community
langchain-openai
pandas
ragas
streamlit
python-dotenv
pypdf
python-docx
```

#### 1.4	Install all dependencies
•	Now, install all the tools we listed in your file. Run this command to start the installation.
```
pip install --upgrade pip
pip install -r requirements.txt
```
<img width="975" height="382" alt="Image" src="https://github.com/user-attachments/assets/11252687-2c5c-42fd-b159-2c25cfbf527d" /> 

##### Dependencies Installed
- fastapi: A high-performance web framework for building APIs with Python.
- uvicorn: An ASGI server that runs your FastAPI application.
- qdrant-client: The official library to connect and talk to the Qdrant vector database.
- sentence-transformers: A framework to turn text into math-based embeddings for semantic search.
- langchain: A toolkit for chaining together LLMs, vector stores, and memory.
- langchain-community: Community-contributed tools and integrations for the LangChain ecosystem.
- langchain-openai: The specific connector used to link LangChain with OpenAI-compatible APIs like Cerebras.
- pandas: A data analysis library used to clean and structure your document information.
- ragas: A framework specifically designed to evaluate the quality of RAG pipelines.
- streamlit: A tool to build and share interactive web dashboards for monitoring.
- python-dotenv: A library that loads your secret API keys from a hidden file.
- pypdf: A tool used to read and extract text from PDF documents.
- python-docx: A library for reading and extracting text from Microsoft Word files.

### Phase 2: Qdrant Vector Database Setup
Phase 2 focuses on setting up Qdrant, the specialized memory for your AI system. Unlike a regular database that stores text or numbers, Qdrant stores high-dimensional vectors that represent the meaning of your documents. By installing it and setting it up as a background service, we ensure your system can perform lightning-fast semantic searches to find relevant information whenever a user asks a question.

#### 2.1	Install Qdrant on VPS using the official binary 
•	Run these commands one by one to download and set up the Qdrant binary on your VPS; Download the latest Qdrant binary
```
wget https://github.com/qdrant/qdrant/releases/latest/download/qdrant-x86_64-unknown-linux-gnu.tar.gz
```
<img width="975" height="447" alt="Image" src="https://github.com/user-attachments/assets/382a5c39-b115-46c7-939a-8b53c5f75cbc" /> 


- Extract the file 
```
tar -xzf qdrant-x86_64-unknown-linux-gnu.tar.gz
```
- Move it to a system folder and make it executable
```
sudo mv qdrant /usr/local/bin/ 
sudo chmod +x /usr/local/bin/qdrant
```

#### 2.2	Configure Qdrant to run on a specific port
•	Create a storage directory for the data. Run;
```
mkdir -p ~/qdrant_storage
```

•	Create the configuration file. Paste the below;
```
cat <<EOF > config.yaml
storage:
  storage_path: ~/qdrant_storage
service:
  http_port: 6333
  grpc_port: 6334
EOF
```
#### 2.3	Create a systemd service to keep Qdrant running 24/7
•	To keep Qdrant running 24/7, even if your server restarts, we will create a systemd service. This acts like a "keep-alive" manager. Paste the below
```
sudo cat <<EOF > /etc/systemd/system/qdrant.service
[Unit]
Description=Qdrant Vector Database
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/projects/ai_ops_system
ExecStart=/usr/local/bin/qdrant --config-path /root/projects/ai_ops_system/config.yaml
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```
•	Now, start the service with these commands:
```
sudo systemctl daemon-reload
sudo systemctl enable qdrant
sudo systemctl start qdrant
```



#### 2.4	Test Qdrant is live and accessible via its REST API
•	To finalize Phase 2, let's make sure we can actually talk to it. Run this command:
```
curl http://localhost:6333
```
<img width="975" height="187" alt="Image" src="https://github.com/user-attachments/assets/cafcd3f6-5ab1-4dc1-a07e-f7a3f78abadc" /> 

Phase 3: Document Ingestion Pipeline
Phase 3 is where we build the machinery to feed your AI the organizational knowledge it needs to be smart. We will create a Python pipeline that acts like a digital shredder and translator: it opens various file types like PDFs and Word docs, extracts the raw text, cleans out the mess, and then breaks that text into small, searchable chunks. By the end of this phase, your system will be able to turn static documents into "live" data stored in Qdrant, allowing the AI to look up specific facts almost instantly.
3.1	Write a text extractor that handles PDF, TXT, and DOCX files
•	Run this command to create a file called ingest.py with the extraction logic:
cat <<EOF > scripts/ingest.py
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
EOF

3.2	Write a text cleaning function to remove noise and broken formatting
•	We will add a function to scripts/ingest.py that uses Regular Expressions (regex) to scrub the text clean. Run this command to append the cleaning logic to your script:
cat <<EOF >> scripts/ingest.py

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
EOF

3.3	Write a chunking function that splits text into meaningful segments with overlap
We can't feed a 50-page document to the AI all at once. We need to split it into smaller "chunks." We also use overlap so that the end of one chunk shares a little bit of text with the start of the next. This ensures no information is cut in half.
•	Run this to add the chunking function to scripts/ingest.py:
cat <<EOF >> scripts/ingest.py

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
EOF

3.4	Tag each chunk with metadata (filename, document type, date, category)
We need to attach labels to each chunk so the AI knows where the information came from (like the filename or date).

•	Run this to add the metadata function to scripts/ingest.py:
cat <<EOF >> scripts/ingest.py

from datetime import datetime

def create_metadata(file_name, category="General"):
    return {
        "filename": file_name,
        "category": category,
        "ingested_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Test metadata
print(f"Metadata sample: {create_metadata('policy.pdf', 'HR')}")
EOF

3.5	Generate embeddings for each chunk using Sentence Transformers
This is where we turn text into math so the computer can understand the meaning. We will use the SentenceTransformer model we installed earlier.
•	Run this to add the embedding logic to scripts/ingest.py. It will download a small, efficient model the first time it runs:
cat <<EOF >> scripts/ingest.py

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
EOF










3.6	Store all embeddings and metadata into Qdrant
Now we need to take those numbers (the embeddings) and the labels (the metadata) and save them into the Qdrant database we set up in Phase 2.
•	Run this to add the storage logic to scripts/ingest.py. We’ll use a "collection" named "ai_ops_docs":
cat <<EOF >> scripts/ingest.py

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
EOF

3.7	Test ingestion with sample documents from each file type
To finish Phase 3, we need to move from "test samples" to a real workflow. We’ll combine everything into a single function that processes a whole file.
•	Run this command to replace the bottom "test" section of scripts/ingest.py with a proper production-ready function:
# First, remove the old test lines (the ones starting with "long_text", "test_chunks", etc.)
# Then, append this robust runner:

cat <<EOF >> scripts/ingest.py

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
EOF
Phase 4: RAG Retrieval Pipeline
Phase 4 is the "intelligence" layer where we transform your stored data into actionable answers. In this phase, we build the RAG (Retrieval-Augmented Generation) Pipeline, which acts as a bridge between your Qdrant vector database and the high-speed Cerebras LLM. We will develop the logic to turn a user's question into a mathematical vector, search for the most relevant "memories" in Qdrant, and feed that specific context into the LLM with strict instructions to answer only based on the provided facts. By the end of this phase, your system won't just find documents; it will read them, reason through them, and provide cited, accurate responses at lightning speed.
4.1 Write a query embedding function using the same Sentence Transformer model
To search Qdrant, we must convert the user's natural language question into the same 384-dimensional vector space used for your documents. We will reuse the SentenceTransformer model to ensure the "math" matches perfectly between the question and the stored data.
•	Run this command to create a new file named scripts/rag_pipeline.py with the query embedding logic:
cat <<EOF > scripts/rag_pipeline.py
import os
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

# Initialize the same model used in Phase 3
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_query(query_text):
    """Converts a user string into a vector embedding."""
    vector = model.encode(query_text).tolist()
    return vector

if __name__ == "__main__":
    # Quick test
    test_query = "How do I reset my password?"
    vector = embed_query(test_query)
    print(f"Query embedded. Vector length: {len(vector)}")
EOF
4.2 Write a retrieval function that searches Qdrant and returns top K relevant chunks with similarity threshold filtering
Next, we write the function that takes that query vector and asks Qdrant to find the most similar text chunks. We will set a Top K (how many results to return) and a Similarity Threshold (to ignore results that aren't relevant enough).
•	Run this to append the retrieval logic to scripts/rag_pipeline.py:
cat <<EOF > scripts/rag_pipeline.py
import os
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

# Initialize model
model = SentenceTransformer('all-MiniLM-L6-v2')
client = QdrantClient(host="localhost", port=6333)

def embed_query(query_text):
    return model.encode(query_text).tolist()

def retrieve_context(query_text, collection_name="test_collection", top_k=3, threshold=0.5):
    query_vector = embed_query(query_text)
    
    # Updated method for newer Qdrant clients
    search_results = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=top_k,
        with_payload=True
    ).points
    
    relevant_chunks = [
        hit for hit in search_results if hit.score >= threshold
    ]
    
    return relevant_chunks

if __name__ == "__main__":
    # Test with the collection we created earlier
    results = retrieve_context("Test chunk content")
    print(f"Retrieved {len(results)} relevant chunks.")
    if results:
        print(f"Top Match Score: {results[0].score}")
        print(f"Content: {results[0].payload.get('text')}")
EOF
4.3 Build a context assembly function that formats retrieved chunks with inline source references and handles the no-context case
Now that we can retrieve raw "points" from Qdrant, we need to format them into a clean block of text that an LLM can actually read. This function will pull the text out of the payload, add inline citations (like "[Source: policy.pdf]"), and handle cases where no relevant information was found.
•	Run this command to append the assembly logic to scripts/rag_pipeline.py
cat <<EOF >> scripts/rag_pipeline.py

def assemble_context(relevant_chunks):
    """Combines retrieved chunks into a single formatted string with citations."""
    if not relevant_chunks:
        return "No relevant context found."
    
    context_parts = []
    for i, hit in enumerate(relevant_chunks):
        text = hit.payload.get("text", "")
        source = hit.payload.get("filename", "Unknown Source")
        # Format: [1] Content... (Source: file.pdf)
        context_parts.append(f"[{i+1}] {text} (Source: {source})")
    
    return "\n\n".join(context_parts)

# Test context assembly
if __name__ == "__main__":
    # Test with existing results
    context_string = assemble_context(results)
    print("\n--- Formatted Context ---")
    print(context_string)
EOF
4.4 Connect Cerebras API as the LLM reasoning engine using LangChain with environment-based API key loading
Now we need to connect the "voice" of your system. Cerebras offers inference at speeds that make RAG feel instant. We will use the langchain-cerebras package to integrate it.
•	LangChain connector for Cerebras. Run;
pip install langchain-cerebras
 
•	You need to make sure your Cerebras API key is available in your environment. Run this in your terminal (replace your_api_key_here with your actual key):
export CEREBRAS_API_KEY="your_api_key_here"
export CEREBRAS_API_KEY="csk-xy48944fxh562pvfd45n4pmcchrx8cyyp5drve4ed9kv9en3"

•	Append the LLM connection logic. Run this to add the Cerebras setup to scripts/rag_pipeline.py;
cat <<EOF >> scripts/rag_pipeline.py

from langchain_cerebras import ChatCerebras

# Initialize the LLM
llm = ChatCerebras(
    model="llama3.1-8b",
    cerebras_api_key=os.environ.get("CEREBRAS_API_KEY")
)

def test_llm_connection():
    """Simple check to ensure Cerebras is responding."""
    try:
        response = llm.invoke("Say 'Cerebras Connected'")
        print(f"LLM Check: {response.content}")
    except Exception as e:
        print(f"LLM Connection Error: {e}")

if __name__ == "__main__":
    test_llm_connection()
EOF
4.5 Write the prompt template that instructs Cerebras to answer using only retrieved context, cite sources, and return an insufficient context response when needed
The prompt is the most critical part of a RAG system. It tells the LLM to stay "inside the box" and only use the documents we provided. If the answer isn't in the context, we want it to admit it rather than making things up.
•	Run this to append the prompt logic to scripts/rag_pipeline.py:
cat <<EOF >> scripts/rag_pipeline.py

from langchain_core.prompts import ChatPromptTemplate

# The system prompt sets the behavior and rules for the LLM
RAG_PROMPT_TEMPLATE = """
You are a specialized AI Operations Assistant. Use the provided context to answer the user question.

Rules:
1. Only use the provided context to answer.
2. If the answer is not in the context, say "I don't have enough information in my database to answer this."
3. Cite the source for each fact you provide (e.g., "Source: manual.pdf").
4. Keep the response professional and concise.

Context:
{context}

Question: {question}
"""

def generate_answer(question, context):
    """Combines prompt, context, and question to get an LLM response."""
    prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)
    chain = prompt | llm
    
    response = chain.invoke({"context": context, "question": question})
    return response.content

# Quick test of the generator
if __name__ == "__main__":
    test_q = "What is the test content?"
    test_c = "[1] Test chunk content (Source: test.pdf)"
    print("\n--- LLM Response ---")
    print(generate_answer(test_q, test_c))
EOF
4.6 Build the full RAG chain: query → validate → embed → retrieve → filter → assemble context → prompt → generate → parse → return structured response with citations and latency
This is the final architectural assembly where we unify every individual component into a single, cohesive RAG engine. This master function handles the entire lifecycle of a request, starting with an input validation check before converting the user query into a vector and searching the Qdrant database. It then filters the results by relevance, assembles the context with precise citations, and feeds the formatted data to the Cerebras LLM for final generation. By structuring the code this way, we create a repeatable pipeline that not only returns an accurate answer but also provides metadata like processing latency and the number of source chunks used.
•	Run this command to update your scripts/rag_pipeline.py with the complete, unified pipeline logic:
cat <<EOF > scripts/rag_pipeline.py
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
2. If the answer is not in the context, say "I don't have enough information in my database to answer this."
3. Cite the source for each fact you provide (e.g., "Source: manual.pdf").
4. Keep the response professional and concise.

Context:
{context}

Question: {question}
"""

def run_rag_pipeline(user_query, collection="test_collection"):
    """
    4.6: Full RAG Chain execution
    Query -> Embed -> Retrieve -> Filter -> Assemble -> Prompt -> Generate -> Parse -> Structured Response
    """
    start_time = time.time()
    
    # 1. Validation & Embedding
    if not user_query.strip():
        return {"error": "Empty query provided"}
    
    query_vector = model.encode(user_query).tolist()
    
    # 2. Retrieve & Filter (Lowered threshold to 0.3 for test stability)
    search_results = client.query_points(
        collection_name=collection,
        query=query_vector,
        limit=3,
        with_payload=True
    ).points
    
    relevant_hits = [hit for hit in search_results if hit.score >= 0.3]
    
    # 3. Assemble Context with Citations
    context_parts = []
    sources_list = []
    for i, hit in enumerate(relevant_hits):
        text = hit.payload.get("text", "")
        source = hit.payload.get("filename", "Unknown Source")
        context_parts.append(f"[{i+1}] {text} (Source: {source})")
        if source not in sources_list:
            sources_list.append(source)
    
    context_text = "\n\n".join(context_parts) if relevant_hits else "No relevant context found."
    
    # 4. Prompt & Generate
    prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)
    chain = prompt | llm
    response = chain.invoke({"context": context_text, "question": user_query})
    
    # 5. Parse & Return Structured Response
    latency = round(time.time() - start_time, 3)
    
    return {
        "status": "success",
        "answer": response.content,
        "metadata": {
            "latency_seconds": latency,
            "chunks_used": len(relevant_hits),
            "citations": sources_list
        }
    }

if __name__ == "__main__":
    print("\n--- Executing Full RAG Chain Test (Step 4.6) ---")
    result = run_rag_pipeline("What is the test content?")
    print(f"Answer: {result['answer']}")
    print(f"Structured Metadata: {result['metadata']}")
EOF
4.7 Test the full RAG chain across three query categories: fully covered, partially covered, and no relevant context
Now that the architecture is locked in, we need to stress-test it across three specific categories to ensure the "brain" knows when to speak and when to stay silent.
The Three Test Scenarios:
Fully Covered: Querying data we know exists (like your "test content").
•	Run this to update the test block
cat <<EOF > scripts/rag_pipeline.py
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
2. If the answer is not in the context, say "I don't have enough information in my database to answer this."
3. Cite the source for each fact you provide (e.g., "Source: manual.pdf").
4. Keep the response professional and concise.

Context:
{context}

Question: {question}
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
    
    context_parts = []
    sources_list = []
    for i, hit in enumerate(relevant_hits):
        text = hit.payload.get("text", "")
        source = hit.payload.get("filename", "Unknown Source")
        context_parts.append(f"[{i+1}] {text} (Source: {source})")
        if source not in sources_list:
            sources_list.append(source)
    
    context_text = "\n\n".join(context_parts) if relevant_hits else "No relevant context found."
    
    prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)
    chain = prompt | llm
    response = chain.invoke({"context": context_text, "question": user_query})
    
    latency = round(time.time() - start_time, 3)
    
    return {
        "answer": response.content,
        "metadata": {
            "latency_seconds": latency,
            "chunks_used": len(relevant_hits),
            "citations": sources_list
        }
    }

if __name__ == "__main__":
    print("\n--- [TEST 1: FULLY COVERED] ---")
    result = run_rag_pipeline("Tell me exactly what the test chunk content says.")
    print(f"Answer: {result['answer']}")
    print(f"Chunks Found: {result['metadata']['chunks_used']}")
    print(f"Sources Cited: {result['metadata']['citations']}")
    print(f"Latency: {result['metadata']['latency_seconds']}s")
EOF
Partially Covered: Querying something similar but not identical to see how the threshold handles it.
•	Run this to update your test block in the terminal:
sed -i 's/result = run_rag_pipeline("Tell me exactly what the test chunk content says.")/result = run_rag_pipeline("Does the test content mention a specific person name?")/' scripts/rag_pipeline.py
python3 scripts/rag_pipeline.py
 






No Relevant Context: Asking a completely unrelated question (e.g., "How do I bake a cake?") to verify the system admits it doesn't know.
•	Run this to update your test block in the terminal:
sed -i 's/result = run_rag_pipeline("Does the test content mention a specific person name?")/result = run_rag_pipeline("What is the best way to bake a chocolate cake?")/' scripts/rag_pipeline.py
python3 scripts/rag_pipeline.py
 


Phase 5: Multi-Agent System
Phase 5 introduces the orchestration layer that transforms a standard retrieval pipeline into an autonomous intelligence system. By implementing a Multi-Agent architecture, the system can move beyond simple question answering to handle complex operational workflows that require reasoning and task delegation. You will develop a Router Agent to act as the central brain, determining whether an incoming request is a straightforward information lookup or a multi-step project requiring the specialized skills of a Task Agent. This phase also integrates conversation memory to ensure the AI maintains context over long interactions, allowing it to support sophisticated decision making and document synthesis across various organizational departments.
5.1 Define the two agent roles: Router Agent and Task Agent
In this step, we define the specialized personalities and logic for our two primary agents: the Router Agent and the Task Agent. Think of the Router as the "Front Desk Manager" who assesses the complexity of an inquiry, while the Task Agent is the "Subject Matter Expert" capable of handling multi-step reasoning and synthesis.
Agent	Role	Responsibility
Router Agent	The Gatekeeper	Analyzes the user's intent to decide if a query can be answered by a simple RAG lookup or if it requires complex task execution.
Task Agent	The Executor	Handles high-level requests such as "Compare the HR policies of 2024 vs 2025" or "Summarize all pending action items from these three reports."

We will use LangChain's Structured Output to ensure the Router Agent returns a machine-readable decision (either rag_pipeline or task_agent).
•	Run the following command to create scripts/agents.py and define these roles:
cat <<EOF > scripts/agents.py
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
EOF

5.2 Build the Router Agent that classifies incoming requests and decides whether to send them to the simple RAG chain or the Task Agent
This focuses on formalizing the Router Agent as a standalone logic module that we can plug into our FastAPI backend later.
The goal here is to ensure the Router doesn't just output a word, but returns a clean, validated decision that our system can use to switch between different code paths.
Run this command to finalize the scripts/router.py file. This separates the "Decision Brain" from the "Execution Body," making your system modular and easier to debug.
cat <<EOF > scripts/router.py
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
EOF
5.3 Build the Task Agent that handles complex multi-step requests involving multiple document collections, sequential tool use, or synthesis across sources
While the RAG pipeline is great for finding a specific needle in a haystack, the Task Agent is designed to look at the entire "haystack" and tell you what it means. In this step, we build the logic for an agent that can handle synthesis, summaries, and cross-document reasoning.
The Task Agent uses a higher "temperature" setting (for more creative synthesis) and a specialized prompt that encourages it to look for patterns, trends, and summaries rather than just single facts.
•	Run this command to create scripts/task_agent.py. This script defines the agent's persona and its 
from the provided test content."
cat <<EOF > scripts/task_agent.py
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
EOF
5.4 Write the routing logic that connects the Router Agent output to the correct downstream handler
Now that the Router (5.2) and the Task Agent (5.3) are both working perfectly as separate units, we need to unify them. Phase 5.4 builds the "Central Command" function that will receive any query and decide which path to take automatically.
Run this command to create the master script scripts/main_agent.py. This script will be the main entry point for your future API.
•	Run this to create scripts/main_agent.py:
cat <<EOF > scripts/main_agent.py
import os
import sys
import time
from scripts.router import get_router_agent
from scripts.task_agent import run_task_agent
from scripts.rag_pipeline import run_rag_pipeline

def execute_ai_ops(user_query, collection="test_collection"):
    """
    Step 5.4: The Unified Multi-Agent Entry Point.
    1. Route the Query
    2. Execute the chosen Handler
    3. Return a consistent structured response
    """
    start_time = time.time()
    
    # 1. Ask the Router for a decision
    router = get_router_agent()
    decision = router.invoke({"question": user_query})
    choice = decision.datasource
    
    print(f"\n[System Log] Router Decision: {choice}")
    
    # 2. Execute based on route
    if choice == "rag_pipeline":
        response = run_rag_pipeline(user_query, collection=collection)
        response["agent_used"] = "RAG Specialist"
    else:
        response = run_task_agent(user_query, collection=collection)
        response["agent_used"] = "Task Specialist"
        
    response["total_latency"] = round(time.time() - start_time, 3)
    return response

if __name__ == "__main__":
    # Test Scenario 1: Simple Fact (RAG)
    print("\n--- TEST 1: FACTUAL ROUTE ---")
    res1 = execute_ai_ops("What is the equipment stipend?")
    print(f"Agent: {res1.get('agent_used')}\nAnswer: {res1['answer']}")

    # Test Scenario 2: Complex Task (Task Agent)
    print("\n--- TEST 2: SYNTHESIS ROUTE ---")
    res2 = execute_ai_ops("Summarize the HR policies for me.")
    print(f"Agent: {res2.get('agent_used')}\nAnswer: {res2['answer']}")
EOF

5.5 Add conversation memory so context is preserved across multi-turn interactions for both the RAG chain and Task Agent
Currently, every time you ask a question, the AI "forgets" who you are or what you just asked. To make this a true assistant, we need Memory.
•	Run this to create a simple memory utility in scripts/memory.py:
cat <<EOF > scripts/memory.py
from langchain.memory import ConversationBufferMemory

# Simple global dictionary to store memory per session
# In a real app, this would be a database like Redis
sessions = {}

def get_session_memory(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = ConversationBufferMemory(
            memory_key="chat_history", 
            return_messages=True
        )
    return sessions[session_id]
EOF
5.6 Wire the full agent pipeline: request → Router Agent → RAG chain or Task Agent → structured response
•	Install langchain community, run;
pip install langchain-community langchain-core
•	Run the below:
cat <<EOF > scripts/memory.py
from langchain.memory import ConversationBufferMemory

# Note: If the above still fails in some environments, 
# LangChain now often uses: from langchain_community.chat_message_histories import ...
# But for standard buffer memory, this is the classic stable import.

sessions = {}

def get_session_memory(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = ConversationBufferMemory(
            memory_key="chat_history", 
            return_messages=True
        )
    return sessions[session_id]
EOF
•	Run this command to create the final version of your main execution logic. This script ensures that if you ask a follow-up question (e.g., "And what about the stipend?"), the AI knows you are still talking about the policy from the previous turn.
cat <<EOF > scripts/main_agent.py
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

def run_ops_intelligence(user_query, session_id="default_user", collection="test_collection"):
    start_time = time.time()
    
    # 1. Load Session Memory
    memory = get_session_memory(session_id)
    history_context = memory.get_history_string()
    
    # 2. Routing Decision
    router = get_router_agent()
    # We pass the query + history context to the router for better awareness
    decision = router.invoke({"question": f"Context: {history_context}\nQuestion: {user_query}"})
    choice = decision.datasource
    
    print(f"\n[Pipeline] Route: {choice} | Session: {session_id}")
    
    # 3. Execution Path
    if choice == "rag_pipeline":
        response_data = run_rag_pipeline(user_query, collection=collection)
        agent_label = "RAG Specialist"
    else:
        response_data = run_task_agent(user_query, collection=collection)
        agent_label = "Task Specialist"
    
    # 4. Save to Memory
    memory.save_context(user_query, response_data["answer"])
    
    return {
        "status": "success",
        "agent": agent_label,
        "answer": response_data["answer"],
        "metadata": {"latency": round(time.time() - start_time, 3)}
    }

if __name__ == "__main__":
    print("--- TURN 1: FACTUAL QUERY ---")
    res1 = run_ops_intelligence("What is the equipment stipend?")
    print(f"[{res1['agent']}] {res1['answer']}")
    
    print("\n--- TURN 2: FOLLOW-UP ---")
    res2 = run_ops_intelligence("And does the policy mention Wednesdays?")
    print(f"[{res2['agent']}] {res2['answer']}")
EOF

5.7 Log every routing decision alongside the query and response so routing performance can be reviewed and improved over time
We will create a specialized logging utility that writes to a CSV-style log file. This makes it incredibly easy to pull the data into your Phase 8 Streamlit dashboard later.
•	Run this command to update your scripts/main_agent.py with the logging integration:
cat <<EOF > scripts/logger.py
import csv
import os
import time

LOG_FILE = "logs/routing_performance.csv"

def initialize_logs():
    """Ensures the log file exists with headers."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
        
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "query", "route_decision", "agent_used", "latency", "status"])

def log_routing_event(query, route, agent, latency, status="success"):
    """Appends a new routing event to the performance log."""
    initialize_logs()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, query, route, agent, latency, status])

if __name__ == "__main__":
    # Test Logging
    log_routing_event("Test Query", "rag_pipeline", "RAG Specialist", 0.45)
    print(f"Logged test event to {LOG_FILE}")
EOF

Now, we modify the main execution function to automatically call this logger every time a request is processed. Run this to update scripts/main_agent.py:
cat <<EOF > scripts/main_agent.py
import os
import sys
import time

# Ensure scripts directory is in path
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
    Standardized Multi-Agent Pipeline with Correct Memory Access
    """
    start_time = time.time()
    
    # 1. Load Session Memory correctly
    memory = get_session_memory(session_id)
    
    # Extracting history string using the native LangChain method
    memory_vars = memory.load_memory_variables({})
    chat_history = memory_vars.get("chat_history", "")
    
    # 2. Routing Decision (Context-Aware)
    router = get_router_agent()
    # We provide the history context so the Router understands follow-ups
    decision = router.invoke({
        "question": f"Chat History: {chat_history}\nUser Query: {user_query}"
    })
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
        response_data = {"answer": f"System Error: {str(e)}", "metadata": {}}
        agent_label = "Error Handler"
        status = "failed"
    
    # 4. Save to Memory (Native LangChain method)
    memory.save_context({"input": user_query}, {"output": response_data["answer"]})
    
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

if __name__ == "__main__":
    # Final Pre-API Stress Test
    print("--- TURN 1: Initial ---")
    print(run_ops_intelligence("What is the equipment stipend?")["answer"])
    
    print("\n--- TURN 2: Follow-up (Context Check) ---")
    print(run_ops_intelligence("And how many days can I work from home?")["answer"])
EOF
Phase 6: FastAPI Backend
Phase 6 marks the transition of your intelligence system from a local script into a production-ready web service. By building a high-performance backend with FastAPI, you provide a standardized gateway that allows external applications, automated workflows, and front-end dashboards to communicate with your AI agents. During this phase, you will implement dedicated endpoints for document ingestion and real-time querying, while securing the system with API key authentication to ensure that only authorized users can access your organizational knowledge. This architectural layer essentially provides the "body" for your AI's "brain," enabling it to be integrated into the broader enterprise ecosystem and handle multiple concurrent requests with low latency and high reliability.
6.1	Create the FastAPI application entry point
We will create main.py in your root project directory. This script initializes the server, defines the data models for incoming requests, and imports the robust agent logic we perfected in Phase 5.
•	Run this command to build your server entry point:
cat <<EOF > main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os
import time

# Ensure the scripts folder is accessible
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from main_agent import run_ops_intelligence

app = FastAPI(
    title="AI Operations Intelligence API",
    description="Cloud-Hosted RAG and Multi-Agent AI System",
    version="1.0.0"
)

# 1. Define the Request Data Model
class QueryRequest(BaseModel):
    query: str
    session_id: str = "default_user"
    collection: str = "test_collection"

# 2. Health Check
@app.get("/")
def read_root():
    return {
        "status": "online", 
        "system": "AI Ops Intelligence",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

# 3. Process Query (Fixed Class Name)
@app.post("/query")
async def process_user_query(request: QueryRequest):
    try:
        result = run_ops_intelligence(
            user_query=request.query, 
            session_id=request.session_id,
            collection=request.collection
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"API Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF
•	Launch the Server: Run this in your terminal
python3 main.py
 

6.2	Build the document upload endpoint that triggers the ingestion pipeline
Now we need to build the "Ingestion Gate." This endpoint will allow you to send actual files (PDF, DOCX, TXT) via an API request. The server will save the file to your data/ folder and immediately trigger the Phase 3 pipeline to extract, chunk, embed, and store the data in Qdrant.
•	To handle file uploads in FastAPI, we need the python-multipart library. Run this first:
pip install python-multipart
 

•	Run this command to add the upload logic to your server. We use shutil to handle the file saving and then call your process_file function:
cat <<EOF > main.py
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
import sys
import os
import shutil
import time

# Ensure scripts folder is accessible
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from main_agent import run_ops_intelligence
from ingest import process_file

app = FastAPI(title="AI Operations Intelligence API")

# 1. Models
class QueryRequest(BaseModel):
    query: str
    session_id: str = "default_user"
    collection: str = "test_collection"

# 2. Health Check
@app.get("/")
def read_root():
    return {"status": "online", "system": "AI Ops Intelligence", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

# 3. Process Query
@app.post("/query")
async def process_user_query(request: QueryRequest):
    try:
        result = run_ops_intelligence(request.query, session_id=request.session_id, collection=request.collection)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query Error: {str(e)}")

# 4. Step 6.2: Document Upload Endpoint
@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...), 
    collection: str = Form("test_collection"), 
    category: str = Form("General")
):
    """
    Receives a file, saves it, and triggers the ingestion pipeline.
    """
    try:
        # Save file to the 'data/' directory
        file_path = os.path.join("data", file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Trigger Ingestion Pipeline (Phase 3)
        process_file(file_path, collection, category)
        
        return {
            "status": "success",
            "filename": file.filename,
            "message": f"File ingested successfully into '{collection}'"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF
6.3	Build the query endpoint that triggers the RAG chain and returns answers
In Phase 6.3, we formalize the Query Endpoint. While we had a basic version in the previous step, we are now refining it to be the production gateway for your RAG (Retrieval-Augmented Generation) system. This endpoint is designed to receive a user's natural language question, pass it through our Multi-Agent router, and return a structured JSON response containing the answer, the agent used, and the source citations.
•	Run this command to refine your query logic in main.py:
cat <<EOF > scripts/main_agent.py
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
EOF
6.4	Build the agent task endpoint that triggers the multi-agent pipeline
We’ll update main.py to add this dedicated route. This ensures that if a user specifically wants an "Executive Summary" or a "Policy Comparison," they can hit a path optimized for higher reasoning.
•	Run this command to append the Task endpoint to your server:
cat <<EOF > main.py
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
import sys
import os
import shutil
import time

# Ensure scripts folder is accessible
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from main_agent import run_ops_intelligence
from ingest import process_file
from task_agent import run_task_agent

app = FastAPI(
    title="AI Operations Intelligence API",
    description="Unified Gateway for RAG and Multi-Agent AI",
    version="1.2.0"
)

class QueryRequest(BaseModel):
    query: str
    session_id: str = "default_user"
    collection: str = "test_collection"

@app.get("/")
def health_check():
    return {"status": "online", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

# Endpoint 1: General Query (Router Decides RAG vs Task)
@app.post("/query")
async def process_general_query(request: QueryRequest):
    try:
        return run_ops_intelligence(request.query, session_id=request.session_id, collection=request.collection)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query Error: {str(e)}")

# Endpoint 2: Specialized Task (Force Task Specialist)
@app.post("/task")
async def execute_task(request: QueryRequest):
    try:
        result = run_task_agent(request.query, collection=request.collection)
        result["session_id"] = request.session_id
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Task Error: {str(e)}")

# Endpoint 3: Document Upload
@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    collection: str = Form("test_collection"), 
    category: str = Form("General")
):
    try:
        file_path = os.path.join("data", file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        process_file(file_path, collection, category)
        return {"status": "success", "message": f"Processed {file.filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF
6.5	Add request logging to save every query, response, and latency to a log file
We will use a Middleware approach. Think of this as a checkpoint at the server's front door: it marks the time when a request arrives, lets the AI do its work, and then calculates the total time spent before the response leaves the building.
•	Run this command to update main.py with the logging logic:
cat <<EOF > main.py
from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Request
from pydantic import BaseModel
import sys
import os
import shutil
import time
import logging

# 1. Setup API Logging
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure a dedicated logger for API traffic
logging.basicConfig(
    filename='logs/api_access.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ensure scripts folder is accessible
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from main_agent import run_ops_intelligence
from ingest import process_file
from task_agent import run_task_agent

app = FastAPI(title="AI Operations Intelligence API")

# 2. Middleware for Request Logging (Step 6.5)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    # Process the request
    response = await call_next(request)
    
    # Calculate duration
    process_time = time.time() - start_time
    
    # Log the event
    log_msg = f"Method: {request.method} | Path: {request.url.path} | Status: {response.status_code} | Duration: {process_time:.3f}s"
    logging.info(log_msg)
    
    # Add the duration to the response headers for transparency
    response.headers["X-Process-Time"] = str(process_time)
    return response

class QueryRequest(BaseModel):
    query: str
    session_id: str = "default_user"
    collection: str = "test_collection"

@app.get("/")
def health_check():
    return {"status": "online", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

@app.post("/query")
async def process_general_query(request: QueryRequest):
    try:
        return run_ops_intelligence(request.query, session_id=request.session_id, collection=request.collection)
    except Exception as e:
        logging.error(f"Query Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Query Error")

@app.post("/task")
async def execute_task(request: QueryRequest):
    try:
        result = run_task_agent(request.query, collection=request.collection)
        result["session_id"] = request.session_id
        return result
    except Exception as e:
        logging.error(f"Task Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Task Error")

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    collection: str = Form("test_collection"), 
    category: str = Form("General")
):
    try:
        file_path = os.path.join("data", file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        process_file(file_path, collection, category)
        return {"status": "success", "message": f"Processed {file.filename}"}
    except Exception as e:
        logging.error(f"Upload Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Ingestion Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF

6.6	Add basic API key authentication to protect all endpoints
We will use a specialized FastAPI tool called APIKeyHeader. It ensures that every single request (Upload, Query, or Task) must include a secret key in the header, or the server will simply refuse to talk.
•	Run this command to update main.py with the security gate:
cat <<EOF > main.py
from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Request, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
import sys, os, shutil, time, logging

# 1. Security Configuration
API_KEY = "admin_secret_key_123"  # Change this to something very long and random later!
API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(header_value: str = Security(api_key_header)):
    if header_value == API_KEY:
        return header_value
    raise HTTPException(status_code=403, detail="Unauthorized: Invalid API Key")

# 2. Setup Logging
if not os.path.exists("logs"): os.makedirs("logs")
logging.basicConfig(filename='logs/api_access.log', level=logging.INFO, format='%(asctime)s - %(message)s')

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from main_agent import run_ops_intelligence
from ingest import process_file
from task_agent import run_task_agent

app = FastAPI(title="Secure AI Ops API")

# Middleware for logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    logging.info(f"{request.method} {request.url.path} - {response.status_code} - {time.time()-start_time:.3f}s")
    return response

class QueryRequest(BaseModel):
    query: str
    session_id: str = "default_user"
    collection: str = "test_collection"

# --- PROTECTED ENDPOINTS (Using Depends) ---

@app.get("/")
def health_check():
    return {"status": "online", "protected": True}

@app.post("/query")
async def process_general_query(request: QueryRequest, token: str = Depends(get_api_key)):
    return run_ops_intelligence(request.query, session_id=request.session_id, collection=request.collection)

@app.post("/task")
async def execute_task(request: QueryRequest, token: str = Depends(get_api_key)):
    result = run_task_agent(request.query, collection=request.collection)
    result["session_id"] = request.session_id
    return result

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    collection: str = Form("test_collection"), 
    category: str = Form("General"),
    token: str = Depends(get_api_key)
):
    file_path = os.path.join("data", file.filename)
    with open(file_path, "wb") as buffer: shutil.copyfileobj(file.file, buffer)
    process_file(file_path, collection, category)
    return {"status": "success", "message": f"Processed {file.filename}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF

6.7	Create a systemd service to keep FastAPI running 24/7
We’re going to tell Linux to treat your AI API as a "System Service." This means it will run silently in the background and restart itself automatically if it ever crashes.
•	Run this command to create the configuration.
sudo cat <<EOF > /etc/systemd/system/ai_ops.service
[Unit]
Description=FastAPI instance for AI Ops System
After=network.target

[Service]
User=root
WorkingDirectory=/root/projects/ai_ops_system
Environment="PATH=/root/projects/ai_ops_system/venv/bin"
Environment="CEREBRAS_API_KEY=key"
ExecStart=/root/projects/ai_ops_system/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
EOF

•	Reload, restart and enable the service. Run;
sudo systemctl daemon-reload
sudo systemctl start ai_ops
sudo systemctl enable ai_ops

•	To confirm everything is running perfectly in the background, run:
sudo systemctl status ai_ops
 

6.8	Open the FastAPI port on the VPS firewall
•	Run these sequentially to open the necessary gates for your API while keeping the rest of the server locked down:
sudo ufw allow 8000/tcp
sudo ufw allow 6333/tcp
sudo ufw allow ssh
sudo ufw enable
sudo ufw status numbered





 

Phase 7: Evaluation with RAGAS
Phase 7 introduces a rigorous quality control layer to your AI system by leveraging the RAGAS (RAG Assessment) framework to mathematically quantify the reliability of your outputs. Moving beyond anecdotal testing, this phase implements automated metrics to evaluate Faithfulness (to ensure the AI isn't hallucinating), Answer Relevance (to confirm user needs are met), and Context Precision (to verify the vector database is retrieving the most pertinent document chunks). By systematically running your pipeline against a curated "ground truth" dataset and logging these scores into a performance CSV, you transform your development process from guesswork into a data-driven operation, ensuring that every answer provided by your multi-Agent system is both factually grounded and operationally sound.
7.1	Prepare a test dataset of questions, ground truth answers, and source documents
To evaluate a RAG system effectively, you cannot rely on vibes alone; you need a "Ground Truth" dataset. This dataset acts as the answer key that the AI's performance is graded against. For RAGAS to work, each test case must contain four specific components: the Question, the Context (the actual text from your docs), the Ground Truth (the perfect human-verified answer), and eventually, the Generated Answer from your LLM.

•	Run this command to create scripts/evaluate_rag.py:
cat <<EOF > scripts/evaluate_rag.py
import pandas as pd
import os

# 7.1: Define the Ground Truth Dataset
# In a production environment, this would be a CSV or JSON file 
# compiled by subject matter experts.
test_data = [
    {
        "question": "What is the equipment stipend amount?",
        "ground_truth": "The company provides a \$500 equipment stipend for remote work setup.",
        "context": "Employees are eligible for a \$500 one-time equipment stipend to set up their home office. (Source: policy.pdf)"
    },
    {
        "question": "Does the policy mention Wednesdays?",
        "ground_truth": "Yes, Wednesdays are designated as 'Deep Work' days with no internal meetings.",
        "context": "To increase productivity, Wednesdays are designated as Deep Work days. No internal meetings should be scheduled. (Source: operations_manual.docx)"
    },
    {
        "question": "What is the reimbursement limit for travel meals?",
        "ground_truth": "The daily limit for travel meal reimbursement is \$75.",
        "context": "Travel expenses include a daily meal allowance capped at \$75 per day. (Source: travel_policy.txt)"
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
EOF








7.2	Run the RAG pipeline on the test dataset and collect all responses and retrieved contexts
Now that we have our "Gold Standard" (the ground truth), we need to put our AI to the test. In this step, we will loop through our test questions, pass them through the actual run_rag_pipeline we built in Phase 4, and record three things:
i. The Answer: What the LLM actually said.
ii. The Contexts: The specific text chunks the system retrieved from Qdrant.
iii. The Latency: How long it took to get the result.
We will update scripts/evaluate_rag.py to include the execution logic. This script will bridge the gap between your test data and your live RAG engine.
•	Run this command to append the execution logic:
cat <<EOF >> scripts/evaluate_rag.py

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
EOF

•	Run this command to update scripts/rag_pipeline.py with an updated version. This version includes the retrieved_contexts key, which is mandatory for the evaluation steps
cat <<EOF > scripts/rag_pipeline.py
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
EOF

7.3	Evaluate Faithfulness (does the answer match the retrieved context)
In RAGAS, Faithfulness is the most critical metric for enterprise AI; it measures if the answer is derived purely from the retrieved context. If the AI says something that isn't in the documents, its faithfulness score drops, signaling a "hallucination."
•	We will create a script that uses the Cerebras LLM as a "Judge" to grade your results. Run this command to create scripts/ragas_scoring.py:
cat <<EOF > scripts/ragas_scoring.py
import pandas as pd
import os
import ast
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevance, context_precision
from langchain_cerebras import ChatCerebras
from datasets import Dataset

# 1. Initialize the Evaluator LLM (The Judge)
llm = ChatCerebras(
    model="llama3.1-8b",
    cerebras_api_key=os.environ.get("CEREBRAS_API_KEY")
)

def run_evaluation_metrics():
    # Load the results generated in Step 7.2
    input_file = "data/eval/results_for_ragas.csv"
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return

    df = pd.read_csv(input_file)
    
    # CRITICAL: Convert the string representation of lists back to actual Python lists
    # CSV saves [text1, text2] as "[text1, text2]" - RAGAS needs the real list.
    df['contexts'] = df['contexts'].apply(ast.literal_eval)

    # Convert to HuggingFace Dataset format (what RAGAS expects)
    eval_dataset = Dataset.from_pandas(df)

    print("\n--- Starting RAGAS Mathematical Evaluation ---")
    print("Metrics: Faithfulness, Answer Relevance, Context Precision")
    
    # 2. Perform the Evaluation
    result = evaluate(
        eval_dataset,
        metrics=[faithfulness, answer_relevance, context_precision],
        llm=llm
    )

    # 3. Save and Display Results
    final_scores_df = result.to_pandas()
    final_scores_df.to_csv("data/eval/final_ragas_report.csv", index=False)
    
    print("\n--- EVALUATION SUMMARY ---")
    print(f"Mean Faithfulness: {final_scores_df['faithfulness'].mean():.4f}")
    print(f"Mean Answer Relevance: {final_scores_df['answer_relevance'].mean():.4f}")
    print(f"Mean Context Precision: {final_scores_df['context_precision'].mean():.4f}")
    print("\nFull report saved to data/eval/final_ragas_report.csv")

if __name__ == "__main__":
    run_evaluation_metrics()
EOF

•	Run this command to fix scripts/ragas_scoring.py:
cat <<EOF > scripts/ragas_scoring.py
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
EOF
7.4	Measure and log response latency for every query
Before we fix the data, let's nail the Performance metric. This is much simpler because it doesn't require an LLM "judge"; it just uses a stopwatch.
•	Run this command to create scripts/benchmarks.py. This will give you the "Production Readiness" numbers you need for your dashboard:
cat <<EOF > scripts/benchmarks.py
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
EOF
7.5	Save all evaluation results to a CSV for the dashboard
Phase 8: Streamlit Monitoring Dashboard
Phase 8 represents the final architectural layer of the system, transforming a complex backend of vector databases and multi-agent logic into a centralized, user-friendly Command Center. By deploying an interactive Streamlit dashboard, you provide stakeholders with a real-time window into the system’s health, visualizing critical RAGAS quality scores and latency trends alongside a secure, password-protected portal for document ingestion and live querying. Implementing this as a persistent background service ensures that the intelligence platform remains accessible 24/7, bridging the gap between sophisticated AI engineering and intuitive operational decision-making.
8.1	Create the Unified Dashboard
The dashboard serves as the "brain's interface," connecting your evaluation logs, the FastAPI backend, and the end-user. By consolidating monitoring, querying, and secure ingestion into one script, we create a seamless workflow where you can oversee performance and manage organizational knowledge from a single URL.
•	Run the following command to create your master dashboard.py file in your project root:
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import os
import time

st.set_page_config(page_title="AI Ops Command Center", layout="wide")
API_URL = "http://localhost:8000"
API_KEY = "admin_secret_key_123" 

st.title("🛡️ AI Operations Command Center")

menu = st.sidebar.radio("Navigation", ["Analytics Dashboard", "Interactive Chat", "Secure Document Upload"])

if menu == "Analytics Dashboard":
    st.header("📈 System Performance & Quality")
    latency_df = pd.read_csv("logs/latency_benchmarks.csv") if os.path.exists("logs/latency_benchmarks.csv") else pd.DataFrame()
    ragas_df = pd.read_csv("data/eval/final_ragas_report.csv") if os.path.exists("data/eval/final_ragas_report.csv") else pd.DataFrame()
    kpi1, kpi2, kpi3 = st.columns(3)
    if not latency_df.empty:
        kpi1.metric("Avg Latency", f"{latency_df['latency'].mean():.2f}s")
        kpi2.metric("Total Queries", len(latency_df))
    if not ragas_df.empty:
        kpi3.metric("Avg Faithfulness", f"{ragas_df['faithfulness'].mean():.2f}")
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        if not latency_df.empty:
            st.line_chart(latency_df.set_index('timestamp')['latency'])
    with c2:
        if not ragas_df.empty:
            avg_scores = ragas_df[['faithfulness', 'answer_relevancy', 'context_precision']].mean().reset_index()
            fig = px.bar(avg_scores, x='index', y=0, range_y=[0,1])
            st.plotly_chart(fig, use_container_width=True)

elif menu == "Interactive Chat":
    st.header("💬 AI Operations Assistant")
    query = st.text_input("Ask a question:")
    if st.button("Query AI"):
        headers = {"X-API-KEY": API_KEY}
        res = requests.post(f"{API_URL}/query", json={"query": query}, headers=headers)
        if res.status_code == 200:
            st.info(res.json()['answer'])

elif menu == "Secure Document Upload":
    st.header("🔐 Secure Data Management")
    access_pass = st.text_input("Admin Password", type="password")
    
    if access_pass == "Osita1989":
        st.success("Access Granted")
        
        # Upload Section
        with st.expander("Upload New Document"):
            uploaded_file = st.file_uploader("Select File")
            coll = st.text_input("Collection", value="test_collection")
            if st.button("Ingest"):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                requests.post(f"{API_URL}/upload", files=files, data={"collection": coll}, headers={"X-API-KEY": API_KEY})
                st.success("Uploaded!")

        st.divider()
        
        # Delete Section
        st.subheader("🗑️ Manage Existing Documents")
        if os.path.exists("data"):
            files_in_dir = [f for f in os.listdir("data") if os.path.isfile(os.path.join("data", f))]
            if files_in_dir:
                for f in files_in_dir:
                    col_file, col_btn = st.columns([3, 1])
                    col_file.write(f)
                    if col_btn.button("Delete", key=f):
                        res = requests.post(f"{API_URL}/delete", data={"filename": f, "collection": "test_collection"}, headers={"X-API-KEY": API_KEY})
                        if res.status_code == 200:
                            st.warning(f"Deleted {f}")
                            time.sleep(1)
                            st.rerun()
            else:
                st.write("No documents found in data/ folder.")

















•	Run the below
streamlit run dashboard.py --server.port 8604 --server.address 0.0.0.0
 

8.2	Create a systemd service to keep the dashboard running 24/7
•	Create the Service File: Run this command to create the ai_dashboard.service file.
sudo cat <<EOF > /etc/systemd/system/ai_dashboard.service
[Unit]
Description=Streamlit Dashboard for AI Ops System
After=network.target ai_ops.service

[Service]
User=root
WorkingDirectory=/root/projects/ai_ops_system
Environment="PATH=/root/projects/ai_ops_system/venv/bin"
ExecStart=/root/projects/ai_ops_system/venv/bin/streamlit run dashboard.py --server.port 8604 --server.address 0.0.0.0
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF



•	Run these three commands to tell Linux to recognize, start, and auto-load the dashboard.
sudo systemctl daemon-reload
sudo systemctl enable ai_dashboard
sudo systemctl start ai_dashboard

•	Check if the dashboard is running successfully in the background:
sudo systemctl status ai_dashboard
 

8.3	Open the dashboard port on the VPS firewall
•	Run these commands;
sudo ufw allow 8604/tcp
sudo ufw status
 


Conclusion
The successful deployment of the Cloud-Hosted RAG and Multi-Agent AI Operations Intelligence System marks a significant transition from manual information retrieval to an automated and intelligent knowledge management framework. By integrating high-performance tools such as Cerebras for reasoning and Qdrant for vector storage, the platform effectively bridges the gap between static organizational data and actionable insights. The implementation of a multi-agent architecture ensures that the system can distinguish between simple factual queries and complex analytical tasks, providing employees with a versatile assistant that enhances productivity and reduces operational bottlenecks across various departments.
Beyond immediate functionality, the inclusion of rigorous evaluation through the RAGAS framework and a centralized Streamlit dashboard establishes a foundation for long-term reliability and continuous improvement. These monitoring tools allow for real-time visibility into system health, response accuracy, and latency, ensuring that the AI remains a trusted source of truth within the enterprise ecosystem. As organizations continue to scale their digital assets, this secure and cloud-native architecture provides the necessary infrastructure to maintain a competitive edge through sophisticated data-driven decision making and streamlined internal workflows.


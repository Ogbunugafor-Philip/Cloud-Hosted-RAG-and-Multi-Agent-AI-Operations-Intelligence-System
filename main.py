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

from qdrant_client.models import Filter, FieldCondition, MatchValue

@app.post("/delete")
async def delete_document(filename: str = Form(...), collection: str = Form("test_collection"), token: str = Depends(get_api_key)):
    try:
        from qdrant_client import QdrantClient
        client = QdrantClient(host="localhost", port=6333)
        
        # Delete points where the metadata 'filename' matches
        client.delete(
            collection_name=collection,
            points_selector=Filter(
                must=[
                    FieldCondition(key="filename", match=MatchValue(value=filename)),
                ]
            ),
        )
        
        # Also remove the physical file from the data folder if it exists
        file_path = os.path.join("data", filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            
        return {"status": "success", "message": f"Deleted {filename} from {collection}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Delete Error: {str(e)}")

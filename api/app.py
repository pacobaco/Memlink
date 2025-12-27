
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from src.middleware import MemLink

app = FastAPI(title="MemLink API")

embed_model = SentenceTransformer('all-MiniLM-L6-v2')
memlink = MemLink(embed_model)

class QueryRequest(BaseModel):
    session_id: str
    user_input: str
    top_k: int = 3

class QueryResponse(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "MemLink API is running."}

@app.post("/query", response_model=QueryResponse)
def query_model(request: QueryRequest):
    try:
        prompt = memlink.query(request.session_id, request.user_input, request.top_k)
        return QueryResponse(prompt=prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

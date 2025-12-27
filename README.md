
# MemLink - Stateful AI Integration Middleware

MemLink is a production-ready middleware that provides:
- Persistent session memory per user/device.
- Vector embeddings for semantic memory retrieval.
- Multi-session and overlay support for multiple accounts.
- Context-aware prompt generation for AI models.
- REST API interface via FastAPI.
- Containerized deployment via Docker/Docker Compose.

## Features
1. Multi-session handling: Each user/device can have independent or shared session memory.
2. Persistent vector memory: Stores embeddings in FAISS for fast similarity search.
3. Overlay support: Multiple accounts can share a base session and apply personal overlays.
4. API endpoints:
    - GET `/` - Health check.
    - POST `/query` - Query session memory and get prompt.
5. Docker support: Ready for containerized deployment.
6. Integration ready: Can integrate with other projects (e.g., Flyometer).

## Quick Start
1. Build Docker image:
```bash
docker-compose build
```
2. Start container:
```bash
docker-compose up
```
3. Query API:
```bash
POST http://localhost:8000/query
{
    "session_id": "user123",
    "user_input": "Explain stateful AI integration",
    "top_k": 3
}
```

## Repo Structure
```
MemLink/
├── src/                  # Core middleware modules
├── api/                  # FastAPI application
├── data/                 # Session data storage
├── examples/             # Example scripts
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Compose file for container orchestration
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project metadata
└── README.md             # This file
```

## License
MIT License

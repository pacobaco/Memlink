
import requests

API_URL = "http://127.0.0.1:8000/query"
payload = {
    "session_id": "user123",
    "user_input": "Explain stateful AI integration",
    "top_k": 3
}

response = requests.post(API_URL, json=payload)
print("Prompt from MemLink API:\n")
print(response.json()["prompt"])

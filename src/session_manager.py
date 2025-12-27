
import os
import json

class SessionManager:
    def __init__(self, storage_path="data/sessions"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)

    def load_session(self, session_id):
        path = os.path.join(self.storage_path, f"{session_id}.json")
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        else:
            return {"history": []}

    def save_session(self, session_id, session_data):
        path = os.path.join(self.storage_path, f"{session_id}.json")
        with open(path, "w") as f:
            json.dump(session_data, f)

    def append_message(self, session_id, message):
        session = self.load_session(session_id)
        session["history"].append(message)
        self.save_session(session_id, session)

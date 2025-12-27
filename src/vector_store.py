
import faiss
import numpy as np
import os
import pickle

class VectorStore:
    def __init__(self, dim, storage_path="data/sessions/vector_store"):
        self.dim = dim
        self.storage_path = storage_path
        self.index_file = os.path.join(storage_path, "faiss.index")
        self.id_file = os.path.join(storage_path, "id_map.pkl")
        os.makedirs(storage_path, exist_ok=True)

        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
            with open(self.id_file, "rb") as f:
                self.id_map = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(dim)
            self.id_map = {}

        self.next_idx = len(self.id_map)

    def add(self, embedding, session_id, message):
        embedding = np.array([embedding], dtype='float32')
        self.index.add(embedding)
        self.id_map[self.next_idx] = (session_id, message)
        self.next_idx += 1
        self._save()

    def query(self, embedding, top_k=3):
        embedding = np.array([embedding], dtype='float32')
        D, I = self.index.search(embedding, top_k)
        results = []
        for idx in I[0]:
            if idx in self.id_map:
                results.append(self.id_map[idx])
        return results

    def _save(self):
        faiss.write_index(self.index, self.index_file)
        with open(self.id_file, "wb") as f:
            pickle.dump(self.id_map, f)

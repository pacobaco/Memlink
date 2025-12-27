
from .state_transformer import EmbeddingTransformer
from .vector_store import VectorStore
from .prompt_builder import PromptBuilder
from .session_manager import SessionManager

class MemLink:
    def __init__(self, embed_model, embed_dim=384):
        self.embed_model = embed_model
        self.transformer = EmbeddingTransformer(embed_dim)
        self.vector_store = VectorStore(embed_dim)
        self.session_manager = SessionManager()

    def query(self, session_id, user_input, top_k=3):
        embedding = self.embed_model.encode([user_input]).astype('float32')
        embedding = self.transformer.transform([embedding])[0]

        session_history = self.session_manager.load_session(session_id)["history"]
        prompt_builder = PromptBuilder(session_history, self.vector_store, self.embed_model)
        prompt = prompt_builder.build_prompt(user_input, top_k)

        self.session_manager.append_message(session_id, user_input)
        self.vector_store.add(embedding, session_id, user_input)

        return prompt

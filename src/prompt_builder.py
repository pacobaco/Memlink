
class PromptBuilder:
    def __init__(self, session_history, vector_store, embed_model):
        self.session_history = session_history
        self.vector_store = vector_store
        self.embed_model = embed_model

    def build_prompt(self, user_input, top_k=3):
        query_vec = self.embed_model.encode([user_input]).astype('float32')
        top_indices = self.vector_store.query(query_vec, top_k)
        memory_context = "\n".join([self.session_history[i] for _, i in enumerate(top_indices)])
        prompt = f"Memory context:\n{memory_context}\n\nConversation so far:\n{chr(10).join(self.session_history)}\nUser: {user_input}\nAI:"
        return prompt

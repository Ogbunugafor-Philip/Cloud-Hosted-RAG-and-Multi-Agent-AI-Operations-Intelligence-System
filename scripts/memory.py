class SimpleMemory:
    def __init__(self):
        self.history = []

    def save_context(self, user_input, ai_output):
        self.history.append({"user": user_input, "ai": ai_output})

    def get_history_string(self):
        return "\n".join([f"User: {m['user']}\nAI: {m['ai']}" for m in self.history])

sessions = {}

def get_session_memory(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = SimpleMemory()
    return sessions[session_id]

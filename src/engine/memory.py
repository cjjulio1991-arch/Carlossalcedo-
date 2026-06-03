import hashlib
import time

class EpisodicMemory:
    def __init__(self):
        self.vector_store = []
        self.compressed_index = {}

    def store_event(self, content: str):
        """
        Stores an event and performs semantic compression if needed.
        """
        timestamp = time.time()
        event_hash = hashlib.sha1(content.encode()).hexdigest()[:8]

        entry = {
            "id": event_hash,
            "timestamp": timestamp,
            "content": content,
            "summary": self._compress(content)
        }

        self.vector_store.append(entry)
        # Keep store lean
        if len(self.vector_store) > 100:
            self.vector_store.pop(0)

        return entry

    def _compress(self, text: str):
        # Simulated semantic compression
        # Extracts key "abstractions"
        words = text.split()
        if len(words) > 10:
            return "Abstraction: " + " ".join(words[:3]) + "..." + words[-1]
        return text

    def recall_relevant(self, query: str):
        # Simulated vector search
        return [e for e in self.vector_store if query.lower() in e["content"].lower()][:3]

episodic_memory = EpisodicMemory()

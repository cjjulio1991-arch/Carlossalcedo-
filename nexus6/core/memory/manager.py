from typing import List, Dict, Any, Optional
from .vector_store import VectorStore
import time

class MemoryManager:
    def __init__(self):
        self.long_term = VectorStore("long_term_knowledge")
        self.experience = VectorStore("experience_logs")
        self.short_term = [] # Simple list for session context

    def store_short_term(self, entry: Dict[str, Any]):
        entry["timestamp"] = time.time()
        self.short_term.append(entry)
        if len(self.short_term) > 50:
            self.short_term.pop(0)

    def store_experience(self, task: str, result: str, success: bool, metadata: Optional[Dict] = None):
        if metadata is None:
            metadata = {}
        metadata.update({"success": success, "timestamp": time.time()})
        self.experience.add_record(
            f"Task: {task} | Result: {result}",
            metadata
        )

    def store_knowledge(self, fact: str, source: str, tags: List[str]):
        self.long_term.add_record(
            fact,
            {"source": source, "tags": ",".join(tags), "timestamp": time.time()}
        )

    def retrieve_context(self, query: str) -> Dict[str, Any]:
        """Retrieve relevant context across memory tiers."""
        kb_results = self.long_term.query(query, n_results=3)
        exp_results = self.experience.query(query, n_results=2)

        return {
            "short_term": self.short_term[-10:], # Last 10 interactions
            "knowledge_base": kb_results,
            "past_experiences": exp_results
        }

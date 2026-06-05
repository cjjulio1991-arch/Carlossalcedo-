import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any, Optional
import uuid

class VectorStore:
    def __init__(self, collection_name: str = "nexus_memory"):
        self.client = chromadb.Client(Settings(allow_reset=True))
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_record(self, text: str, metadata: Dict[str, Any], id: Optional[str] = None):
        if not id:
            id = str(uuid.uuid4())
        self.collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[id]
        )

    def query(self, query_text: str, n_results: int = 5) -> List[Dict[str, Any]]:
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        # Format results for easier consumption
        formatted = []
        if results['documents']:
            for i in range(len(results['documents'][0])):
                formatted.append({
                    "content": results['documents'][0][i],
                    "metadata": results['metadatas'][0][i],
                    "distance": results['distances'][0][i] if 'distances' in results else None
                })
        return formatted

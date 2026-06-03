import threading
import time

class SystemState:
    def __init__(self):
        self._state = {
            "coherence_index": 0.0,
            "status": "INITIALIZING",
            "memory_nodes": 0,
            "timestamp": time.time()
        }
        self._lock = threading.Lock()

    def update(self, **kwargs):
        with self._lock:
            self._state.update(kwargs)
            self._state["timestamp"] = time.time()

    def get_all(self):
        with self._lock:
            return self._state.copy()

# Singleton instance for shared access
shared_state = SystemState()

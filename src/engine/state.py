import threading
import time

class SystemState:
    def __init__(self):
        self._state = {
            "status": "INITIALIZING",
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

    def get(self, key, default=None):
        with self._lock:
            return self._state.get(key, default)

# Singleton instance for shared access
shared_state = SystemState()

import pytest
import time
from src.engine.state import SystemState

def test_state_initialization():
    state = SystemState()
    data = state.get_all()
    assert data["coherence_index"] == 0.0
    assert data["status"] == "INITIALIZING"

def test_state_update():
    state = SystemState()
    state.update(coherence_index=0.99, status="ACTIVE")
    data = state.get_all()
    assert data["coherence_index"] == 0.99
    assert data["status"] == "ACTIVE"
    assert data["timestamp"] > 0

def test_thread_safety_smoke():
    # Simple smoke test for concurrent updates
    state = SystemState()
    import threading

    def updater():
        for i in range(100):
            state.update(memory_nodes=i)

    threads = [threading.Thread(target=updater) for _ in range(10)]
    for t in threads: t.start()
    for t in threads: t.join()

    data = state.get_all()
    assert 0 <= data["memory_nodes"] < 100

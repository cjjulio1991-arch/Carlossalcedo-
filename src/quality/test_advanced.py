import pytest
import time
from src.engine.math_engine import calculate_system_metrics
from src.security.resilience import ResilienceSystem
from src.orchestration.orchestrator import Orchestrator

def test_math_engine_deterministic():
    metrics1 = calculate_system_metrics()
    time.sleep(0.1)
    metrics2 = calculate_system_metrics()
    # Metrics should be different due to time-based calculation
    assert metrics1["coherence_index"] != metrics2["coherence_index"]
    assert "cognitive_load" in metrics1

def test_resilience_hashing():
    rs = ResilienceSystem()
    state = {"data": "test"}
    backup1 = rs.create_rolling_backup(state)
    backup2 = rs.create_rolling_backup(state)

    assert backup1["hash"] != backup2["hash"]
    assert backup2["prev_hash"] == backup1["hash"]
    assert len(rs.history) == 2

def test_orchestrator_cycle():
    from src.engine.state import shared_state
    success = Orchestrator.step()
    assert success
    data = shared_state.get_all()
    assert "last_backup_hash" in data
    assert len(data["last_backup_hash"]) == 64

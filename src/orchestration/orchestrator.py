from src.engine.state import shared_state
from src.engine.math_engine import calculate_system_metrics
from src.security.resilience import resilience_monitor

class Orchestrator:
    @staticmethod
    def step():
        """
        Executes a single cognitive cycle:
        1. Calculate advanced metrics.
        2. Update global state.
        3. Perform resilience backup.
        """
        try:
            # 1. Math Engine processing
            metrics = calculate_system_metrics()

            # 2. State update
            shared_state.update(**metrics)

            # 3. Security/Resilience layer
            current_state = shared_state.get_all()
            backup = resilience_monitor.create_rolling_backup(current_state)

            shared_state.update(
                last_backup_hash=backup.get("hash"),
                resilience_status=backup.get("status")
            )

            return True
        except Exception as e:
            print(f"Orchestration Error: {e}")
            shared_state.update(status="ERROR", last_error=str(e))
            return False

orchestrator = Orchestrator()

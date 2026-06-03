from src.engine.state import shared_state
from src.engine.math_engine import calculate_system_metrics
from src.security.resilience import resilience_monitor
from src.engine.deep_rl import dqn_engine

class Orchestrator:
    @staticmethod
    def step():
        """
        Executes a single cognitive cycle:
        1. Calculate advanced mathematical metrics.
        2. Execute DQN Deep RL action selection.
        3. Update global state and perform resilience backup.
        """
        try:
            # 1. Math Engine processing
            metrics = calculate_system_metrics()

            # 2. Deep RL processing
            state_vector = [metrics["coherence_index"], metrics["memory_nodes"], metrics["flow_rate"]]
            rl_action = dqn_engine.act(state_vector)
            dqn_engine.replay(batch_size=32) # Simulate learning

            # 3. State update
            shared_state.update(**metrics)
            shared_state.update(
                rl_action=rl_action,
                rl_epsilon=round(dqn_engine.epsilon, 4)
            )

            # 4. Security/Resilience layer
            current_state = shared_state.get_all()
            backup = resilience_monitor.create_rolling_backup(current_state)

            shared_state.update(
                last_backup_hash=backup.get("hash"),
                resilience_status=backup.get("status"),
                mythos_guard_status=backup.get("mythos_guard", "INACTIVE")
            )

            return True
        except Exception as e:
            print(f"Orchestration Error: {e}")
            shared_state.update(status="ERROR", last_error=str(e))
            return False

orchestrator = Orchestrator()

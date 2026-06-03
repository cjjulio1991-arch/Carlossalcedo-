from src.engine.state import shared_state
from src.engine.math_engine import calculate_system_metrics
from src.security.resilience import resilience_monitor
from src.engine.deep_rl import dqn_engine
from src.orchestration.swarm import swarm_orchestrator
from src.engine.router import cognitive_router
from src.engine.memory import episodic_memory
from src.engine.vision import multimodal_vision
from src.engine.tools import autonomous_tools
from src.orchestration.debate import cognitive_debate
from src.agents.immunology import immunology_agent
from src.engine.forge import forge

class Orchestrator:
    @staticmethod
    def step():
        """
        Executes a single cognitive cycle:
        1. Calculate advanced mathematical metrics.
        2. Execute DQN Deep RL action selection.
        3. Swarm Orchestration (Multi-agent tasking).
        4. Update global state and perform resilience backup.
        """
        try:
            # 0. Cognitive Routing (Polyglot)
            routing_info = cognitive_router.route_task("Perform full system audit and optimization cycle")

            # 1. Math Engine processing
            metrics = calculate_system_metrics()

            # 2. Deep RL processing
            state_vector = [metrics["coherence_index"], metrics["memory_nodes"], metrics["flow_rate"]]
            rl_action = dqn_engine.act(state_vector)
            dqn_engine.replay(batch_size=32) # Simulate learning

            # 3. Swarm Hive processing
            swarm_results = swarm_orchestrator.process_complex_problem("System Optimization Cycle")

            # 3.5 Episodic Memory Storage
            event_summary = f"Cycle executed with model {routing_info['model']}. Swarm results: {len(swarm_results)}"
            episodic_memory.store_event(event_summary)

            # 3.6 Multimodal & Tools
            vision_data = multimodal_vision.analyze_perception("System Dashboard Capture")
            tool_execution = autonomous_tools.execute_safe_script("print('Optimizing system variables...')")

            # 3.7 Adversarial Debate
            debate_result = cognitive_debate.resolve_complex_decision("Update Meta-Optimization Axioms")

            # 3.8 Meta-Optimization
            meta_log = dqn_engine.meta_optimizer.evaluate_and_adjust(metrics["stability"])

            # 3.9 Immunology (Self-Healing)
            immunology_agent.monitor_and_heal()

            # 4.0 Recursive Self-Improvement (The Forge)
            improvement_log = forge.execute_self_improvement()

            # 4. State update
            shared_state.update(**metrics)
            shared_state.update(
                rl_action=rl_action,
                rl_epsilon=round(dqn_engine.epsilon, 4),
                swarm_activity=[r["result"] for r in swarm_results],
                active_model=routing_info["model"],
                routing_tier=routing_info["tier"],
                memory_size=len(episodic_memory.vector_store),
                perception_log=vision_data["analysis"],
                last_tool_status=tool_execution["status"],
                last_debate_status=debate_result["decision"],
                consensus_score=debate_result["consensus_score"],
                meta_control_log=meta_log,
                forge_status=improvement_log
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

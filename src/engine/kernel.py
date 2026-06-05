import time
from src.orchestration.orchestrator import orchestrator
from src.engine.state import shared_state
from src.security.resource_manager import resource_manager

def kernel_process():
    """
    AetherOS Core Execution Loop.
    Enforces resource stabilization based on real system telemetry.
    """
    # Enforce POSIX limits for the kernel thread
    resource_manager.enforce_limits()

    while True:
        try:
            # Execute one orchestration step (Telemetry + Security Audit)
            orchestrator.step()

            # Simple stabilization logic: If CPU > 90%, slow down processing
            current_cpu = shared_state.get('cpu_percent', 0.0)
            if current_cpu > 90.0:
                time.sleep(5)
            else:
                time.sleep(2)

        except Exception as e:
            print(f"Kernel Error: {e}")
            time.sleep(5)

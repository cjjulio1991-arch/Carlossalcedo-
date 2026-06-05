import time
from src.engine.state import shared_state
from src.engine.system_telemetry import telemetry
from src.tools.security_scanner import security_scanner
from src.tools.process_manager import process_manager
from src.security.resilience import resilience_monitor

class Orchestrator:
    def __init__(self):
        self.prev_cpu = None

    def step(self):
        """
        Executes a functional system audit cycle:
        1. Gather real-time system telemetry.
        2. Perform security audit.
        3. Monitor running processes.
        4. Update global state.
        """
        try:
            # 1. Gather Telemetry
            metrics = telemetry.get_all_metrics(self.prev_cpu)
            self.prev_cpu = metrics.get("cpu_raw")

            # 2. Security Audit
            security_data = security_scanner.run_full_audit()

            # 3. Process Management
            proc_data = process_manager.get_running_processes(limit=10)

            # 4. Update Shared State
            shared_state.update(
                cpu_percent=metrics["cpu_percent"],
                memory_used_mb=metrics["memory"]["used_mb"],
                memory_percent=metrics["memory"]["percent"],
                load_avg=metrics["load_avg"],
                security_issues=len(security_data["world_writable"]),
                active_listeners=len(security_data["active_listeners"]),
                process_list=proc_data.get("processes", []),
                security_audit_log=security_data
            )

            # Resilience Snapshot (Functional State)
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

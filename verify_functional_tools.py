import sys
import os

# Ensure the root 'src' is in the path
sys.path.append(os.path.join(os.getcwd(), "src"))
sys.path.append(os.getcwd())

from src.engine.system_telemetry import telemetry
from src.tools.security_scanner import security_scanner
from src.tools.process_manager import process_manager

def test_functional_tools():
    print("Testing Functional Tools...")

    # 1. Test Telemetry
    print("\n[1/3] Testing Telemetry Engine...")
    metrics = telemetry.get_all_metrics()
    print(f"Metrics: {metrics}")
    assert "cpu_percent" in metrics
    assert "memory" in metrics
    assert metrics["memory"]["total_mb"] > 0
    print("Telemetry Engine: OK")

    # 2. Test Security Scanner
    print("\n[2/3] Testing Security Scanner...")
    audit = security_scanner.run_full_audit()
    print(f"Audit Results (Summary): {len(audit['world_writable'])} writable files, {len(audit['active_listeners'])} listeners.")
    assert "world_writable" in audit
    assert "active_listeners" in audit
    print("Security Scanner: OK")

    # 3. Test Process Manager
    print("\n[3/3] Testing Process Manager...")
    procs = process_manager.get_running_processes(limit=5)
    assert "processes" in procs
    print(f"Processes found: {len(procs['processes'])}")
    for p in procs['processes']:
        print(f"  - {p[:100]}")
    print("Process Manager: OK")

    print("\nAll functional tools passed verification.")

if __name__ == "__main__":
    try:
        test_functional_tools()
    except Exception as e:
        print(f"Verification FAILED: {e}")
        sys.exit(1)

import time
from src.orchestration.orchestrator import orchestrator

def kernel_process():
    """
    Core execution loop.
    Delegates processing to the Orchestrator for advanced cognitive cycles.
    """
    while True:
        orchestrator.step()
        time.sleep(1)

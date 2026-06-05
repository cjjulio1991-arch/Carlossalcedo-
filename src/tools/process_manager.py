import subprocess

class ProcessManager:
    """
    Functional process management and monitoring.
    """

    @staticmethod
    def get_running_processes(limit=20):
        """Returns a list of running processes using 'ps aux'."""
        try:
            # Sort by CPU usage
            result = subprocess.run(['ps', 'aux', '--sort=-%cpu'], capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                header = lines[0]
                procs = lines[1:limit+1]
                return {"header": header, "processes": procs}
        except FileNotFoundError:
            return {"error": "ps command not found"}
        except Exception as e:
            return {"error": str(e)}
        return {"error": "unknown error"}

process_manager = ProcessManager()

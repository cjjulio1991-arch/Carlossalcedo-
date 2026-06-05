import os
import subprocess

class SecurityScanner:
    """
    Functional security scanner for professional auditing.
    """

    @staticmethod
    def find_world_writable_files(root_dir="."):
        """Identifies files with world-writable permissions (777/666)."""
        writable_files = []
        try:
            for root, dirs, files in os.walk(root_dir):
                for name in files:
                    filepath = os.path.join(root, name)
                    try:
                        mode = os.stat(filepath).st_mode
                        if mode & 0o002: # World writable bit
                            writable_files.append(filepath)
                    except (PermissionError, FileNotFoundError):
                        continue
        except Exception:
            pass
        return writable_files

    @staticmethod
    def get_active_listeners():
        """Lists active network listeners via netstat."""
        try:
            # Using -lntu for Listening, Numeric, TCP, UDP
            result = subprocess.run(['netstat', '-lntu'], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip().split('\n')[2:] # Skip header
        except FileNotFoundError:
            return ["netstat not found"]
        except Exception as e:
            return [f"Error: {e}"]
        return []

    @staticmethod
    def run_full_audit():
        return {
            "world_writable": SecurityScanner.find_world_writable_files(),
            "active_listeners": SecurityScanner.get_active_listeners()
        }

security_scanner = SecurityScanner()

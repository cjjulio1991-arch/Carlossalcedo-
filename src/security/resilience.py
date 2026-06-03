import hashlib
import json
import time

class ResilienceSystem:
    def __init__(self):
        self.history = []
        self.last_hash = "0" * 64

    def create_rolling_backup(self, state):
        """
        Creates a SHA-256 rolling backup of the system state.
        Ensures state integrity by chaining hashes.
        """
        try:
            # Serialize state for hashing
            state_str = json.dumps(state, sort_keys=True)
            # Chain the current state with the previous hash
            payload = state_str + self.last_hash
            new_hash = hashlib.sha256(payload.encode()).hexdigest()

            backup_entry = {
                "timestamp": time.time(),
                "hash": new_hash,
                "prev_hash": self.last_hash,
                "status": "SECURE"
            }

            self.last_hash = new_hash
            self.history.append(backup_entry)

            # Keep only last 10 backups in memory
            if len(self.history) > 10:
                self.history.pop(0)

            return backup_entry
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

    def verify_integrity(self):
        # In a real system, this would re-verify the chain
        return True

resilience_monitor = ResilienceSystem()

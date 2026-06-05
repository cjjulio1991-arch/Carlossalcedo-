import re

class FormalVerifier:
    """
    Code Safety Scanner.
    Checks for high-risk patterns before execution.
    """
    def __init__(self):
        self.risk_patterns = {
            "OS_DELETE": r"os\.remove|shutil\.rmtree",
            "RECURSIVE_LOOP": r"while True"
        }

    def verify_action(self, code: str):
        """
        Scans code for risk patterns.
        """
        violations = []
        for risk, pattern in self.risk_patterns.items():
            if re.search(pattern, code):
                violations.append(risk)

        if violations:
            return {
                "status": "FORBIDDEN",
                "violations": violations
            }

        return {
            "status": "VERIFIED"
        }

formal_verifier = FormalVerifier()

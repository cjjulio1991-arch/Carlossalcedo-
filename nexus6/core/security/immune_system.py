import ast
from typing import Dict, Any, List

class CognitiveImmuneSystem:
    """
    Detects errors, blocks corrupt info, and measures confidence in decisions.
    """
    def __init__(self):
        self.health_metrics = {"integrity": 1.0, "noise_level": 0.05}

    def validate_proposal(self, proposal: Dict[str, Any]) -> Dict[str, Any]:
        # Consensus-based confidence scoring
        confidence = proposal.get("confidence", 0.0)

        # Security & Logic Scan
        safety_report = self._perform_deep_scan(proposal)

        if not safety_report["safe"]:
            return {
                "authorized": False,
                "reason": f"Security Violation: {safety_report['reason']}",
                "confidence_adjustment": -0.5
            }

        # Confidence threshold
        if confidence < 0.7:
             return {
                "authorized": False,
                "reason": "Insufficient confidence score for autonomous execution.",
                "confidence_adjustment": 0.0
            }

        return {
            "authorized": True,
            "confidence_adjustment": 0.0,
            "health_status": self.health_metrics
        }

    def _perform_deep_scan(self, proposal: Dict[str, Any]) -> Dict[str, Any]:
        content = str(proposal.get("solution", ""))

        # Static Analysis for forbidden patterns (Simulated)
        forbidden_patterns = ["rm -rf", "eval(", "exec(", "os.system"]
        for pattern in forbidden_patterns:
            if pattern in content:
                return {"safe": False, "reason": f"Detected forbidden pattern: {pattern}"}

        return {"safe": True}

    def update_health(self):
        # Autonomous self-healing logic
        self.health_metrics["integrity"] = min(1.0, self.health_metrics["integrity"] + 0.01)
        self.health_metrics["noise_level"] = max(0.0, self.health_metrics["noise_level"] - 0.005)

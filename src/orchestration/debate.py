from src.agents.specialized_agents import ResearcherAgent, ValidatorAgent
import random

class CognitiveDebate:
    def __init__(self):
        self.creator = ResearcherAgent()
        self.skeptic = ValidatorAgent()

    def resolve_complex_decision(self, proposition: str):
        """
        Facilitates an adversarial debate between two agents to reach consensus.
        """
        rounds = 3
        debate_log = []

        for i in range(rounds):
            # Phase 1: Creator proposes
            proposal = self.creator.execute(f"Propose solution for {proposition} (Round {i+1})")
            debate_log.append(f"Creator: {proposal}")

            # Phase 2: Skeptic critiques
            critique = self.skeptic.execute(f"Find flaws in: {proposal}")
            debate_log.append(f"Skeptic: {critique}")

        # Final consensus evaluation (Simulated)
        consensus_score = random.uniform(0.7, 0.95)
        decision = "APPROVED" if consensus_score > 0.8 else "REVISED_REQUIRED"

        return {
            "proposition": proposition,
            "decision": decision,
            "consensus_score": round(consensus_score, 3),
            "log": debate_log
        }

cognitive_debate = CognitiveDebate()

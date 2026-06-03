from src.agents.specialized_agents import ResearcherAgent, CoderAgent, ValidatorAgent
import json

class SwarmOrchestrator:
    def __init__(self):
        self.agents = {
            "research": ResearcherAgent(),
            "coding": CoderAgent(),
            "validation": ValidatorAgent()
        }

    def process_complex_problem(self, problem: str):
        """
        Divides a problem and assigns tasks to the swarm.
        """
        # Simulated task decomposition
        subtasks = [
            {"agent": "research", "task": f"Gather context for {problem}"},
            {"agent": "coding", "task": f"Implement solution for {problem}"},
            {"agent": "validation", "task": f"Audit solution for {problem}"}
        ]

        results = []
        for sub in subtasks:
            agent = self.agents[sub["agent"]]
            result = agent.execute(sub["task"])
            results.append({"agent": agent.name, "result": result})

        return results

swarm_orchestrator = SwarmOrchestrator()

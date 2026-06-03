from src.agents.specialized_agents import ResearcherAgent, CoderAgent, ValidatorAgent
from src.agents.morphogenesis import morphogenesis_engine
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
        Includes Morphogenesis for unknown domains.
        """
        # Morphogenesis Check
        dynamic_agents = []
        if "ultra-específica" in problem.lower():
            new_agent = morphogenesis_engine.create_ephemeral_agent(
                "SpecialistX", "Hyper-Optimization", "Optimize specific flux vector A1"
            )
            self.agents["specialist_x"] = new_agent
            dynamic_agents.append("specialist_x")

        # Simulated task decomposition
        subtasks = [
            {"agent": "research", "task": f"Gather context for {problem}"},
            {"agent": "coding", "task": f"Implement solution for {problem}"},
            {"agent": "validation", "task": f"Audit solution for {problem}"}
        ]

        results = []
        for sub in subtasks:
            agent = self.agents.get(sub["agent"])
            if agent:
                result = agent.execute(sub["task"])
                results.append({"agent": agent.name, "result": result})

        # Cleanup ephemeral agents
        for dag in dynamic_agents:
            morphogenesis_engine.cleanup_agent("SpecialistX")
            del self.agents[dag]

        return results

swarm_orchestrator = SwarmOrchestrator()

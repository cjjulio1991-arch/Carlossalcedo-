from typing import Dict, Any, List
from nexus6.core.agents.specialized import AnalystAgent, EngineerAgent, ScientistAgent, AuditorAgent
from nexus6.core.memory.manager import MemoryManager
from nexus6.core.reasoning.first_principles import FirstPrincipleEngine
from nexus6.core.reasoning.creative_synthesis import CreativeSynthesisEngine
from nexus6.core.reasoning.pattern_intelligence import PatternIntelligenceModule
from nexus6.core.security.immune_system import CognitiveImmuneSystem
from nexus6.core.tools.orchestrator import ToolOrchestrator
import asyncio
import uuid

class IntelligenceEngine:
    def __init__(self):
        self.memory = MemoryManager()
        self.immune_system = CognitiveImmuneSystem()
        self.orchestrator = ToolOrchestrator()

        # Reasoning Modules
        self.first_principles = FirstPrincipleEngine()
        self.creative_synth = CreativeSynthesisEngine()
        self.pattern_intel = PatternIntelligenceModule()

        # Agents
        self.analyst = AnalystAgent("Analyst-01", "Analyst", "Detect patterns and extract facts")
        self.engineer = EngineerAgent("Engineer-01", "Engineer", "Design and optimize solutions")
        self.scientist = ScientistAgent("Scientist-01", "Scientist", "Simulate and validate models")
        self.auditor = AuditorAgent("Auditor-01", "Auditor", "Safety and consistency review")

    async def solve_problem(self, problem: str) -> Dict[str, Any]:
        task_id = str(uuid.uuid4())

        # 1. First Principles Decomposition
        fp_analysis = self.first_principles.decompose(problem)
        self.memory.store_short_term({"step": "first_principles", "data": fp_analysis})

        # 2. Pattern Intelligence
        patterns = self.pattern_intel.detect_patterns([problem])

        # 3. Agent Collaboration Cycle
        # Analyst
        analysis_action = await self.analyst.think({"problem": problem, "fp": fp_analysis})
        analysis_res = await self.orchestrator.execute(analysis_action.tool, **analysis_action.tool_input)
        analysis_final = await self.analyst.process_result(analysis_res)

        # Engineer
        eng_action = await self.engineer.think({"analysis": analysis_final.output})
        eng_res = await self.orchestrator.execute(eng_action.tool, **eng_action.tool_input)
        eng_final = await self.engineer.process_result(eng_res)

        # Creative Synthesis
        innovation = self.creative_synth.synthesize(problem)

        # Auditor / Immune System Check
        final_proposal = {
            "task_id": task_id,
            "solution": eng_final.output,
            "innovation": innovation,
            "confidence": (analysis_final.confidence + eng_final.confidence) / 2
        }

        validation = self.immune_system.validate_proposal(final_proposal)

        if validation["authorized"]:
            self.memory.store_experience(problem, str(final_proposal["solution"]), True)
            return {
                "status": "SUCCESS",
                "result": final_proposal,
                "validation": validation
            }
        else:
            return {
                "status": "BLOCKED",
                "reason": validation["reason"]
            }

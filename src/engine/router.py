import random

class CognitiveRouter:
    def __init__(self):
        self.models = {
            "PRO": ["Claude-3.5-Sonnet", "GPT-4o"],
            "LITE": ["Mistral-7B", "Llama-3-8B-Instant"]
        }

    def route_task(self, task_description: str):
        """
        Evaluates task complexity and assigns the optimal model.
        """
        complexity_score = self._evaluate_complexity(task_description)

        if complexity_score > 7:
            selected_model = random.choice(self.models["PRO"])
            tier = "High-Intelligence (PRO)"
        else:
            selected_model = random.choice(self.models["LITE"])
            tier = "Efficiency-Optimized (LITE)"

        return {
            "task": task_description,
            "model": selected_model,
            "tier": tier,
            "complexity": complexity_score
        }

    def _evaluate_complexity(self, text: str):
        # Simulated heuristic for complexity evaluation
        base_score = len(text.split()) / 5
        # Keywords that increase complexity
        if any(kw in text.lower() for kw in ["arquitectura", "seguridad", "código", "optimización"]):
            base_score += 4
        return min(10, round(base_score, 1))

cognitive_router = CognitiveRouter()

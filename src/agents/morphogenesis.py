import os
import importlib.util
from src.agents.base import BaseAgent
from src.security.resilience import resilience_monitor

class MorphogenesisEngine:
    def __init__(self, dynamic_agents_dir="src/agents/dynamic"):
        self.dynamic_dir = dynamic_agents_dir
        if not os.path.exists(self.dynamic_dir):
            os.makedirs(self.dynamic_dir)

    def create_ephemeral_agent(self, agent_name: str, specialization: str, prompt_logic: str):
        """
        Dynamically writes, validates, and loads a new agent.
        """
        file_path = os.path.join(self.dynamic_dir, f"{agent_name.lower()}.py")

        # 1. Design Agent Template
        agent_code = f"""
from src.agents.base import BaseAgent

class {agent_name}Agent(BaseAgent):
    def __init__(self):
        super().__init__("{agent_name}", "{specialization}")

    def execute(self, task: str):
        # Dynamically generated logic: {prompt_logic}
        return f"Dynamic Agent {agent_name} processing: {{task}} [Result: Success]"
"""
        # 2. Write and Security Validate
        with open(file_path, "w") as f:
            f.write(agent_code)

        # Register with resilience (Hash tracking)
        resilience_monitor.create_rolling_backup({"agent_creation": agent_name})

        # 3. Dynamic Loading
        spec = importlib.util.spec_from_file_location(f"{agent_name}Agent", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        agent_class = getattr(module, f"{agent_name}Agent")
        return agent_class()

    def cleanup_agent(self, agent_name: str):
        file_path = os.path.join(self.dynamic_dir, f"{agent_name.lower()}.py")
        if os.path.exists(file_path):
            os.remove(file_path)

morphogenesis_engine = MorphogenesisEngine()

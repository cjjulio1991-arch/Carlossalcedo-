from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class AgentAction(BaseModel):
    tool: str
    tool_input: Dict[str, Any]
    thought: str

class AgentResult(BaseModel):
    output: Any
    confidence: float
    metadata: Dict[str, Any] = {}

class BaseAgent(ABC):
    def __init__(self, name: str, role: str, goal: str):
        self.name = name
        self.role = role
        self.goal = goal

    @abstractmethod
    async def think(self, context: Dict[str, Any]) -> AgentAction:
        """Process context and decide on an action."""
        pass

    @abstractmethod
    async def process_result(self, result: Any) -> AgentResult:
        """Process the result of an action."""
        pass

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from pydantic import BaseModel

class ToolMetadata(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Any]

class BaseTool(ABC):
    @property
    @abstractmethod
    def metadata(self) -> ToolMetadata:
        pass

    @abstractmethod
    async def run(self, **kwargs) -> Any:
        """Execute the tool's core logic."""
        pass

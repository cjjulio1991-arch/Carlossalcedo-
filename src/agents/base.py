from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    def execute(self, task: str):
        pass

    def __repr__(self):
        return f"Agent(name={self.name}, role={self.role})"

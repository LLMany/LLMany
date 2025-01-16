from abc import ABC, abstractmethod


class LLManyRequest(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

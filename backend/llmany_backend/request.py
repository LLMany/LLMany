from abc import ABC, abstractmethod


class Request(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

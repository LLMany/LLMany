from abc import ABC, abstractmethod


class ModelHandler(ABC):
    @abstractmethod
    def send_message(self, message: str) -> None:
        pass

    @abstractmethod
    def parse_message(self) -> str:
        return ...

from abc import ABC, abstractmethod


class ModelHandler(ABC):
    @abstractmethod
    def send_message(
        self, model: str, message: str, history: list[dict[str, str]]
    ) -> str:
        pass

    @abstractmethod
    def parse_message(self) -> str:
        pass

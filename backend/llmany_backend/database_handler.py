from typing import Tuple, Dict
from abc import ABC, abstractmethod


class DatabaseHandler(ABC):
    @abstractmethod
    def get_model_for_chat(self, id: str) -> Tuple[str, str]:
        pass

    @abstractmethod
    def create_new_chat(self, model_type: str, model: str) -> int:
        pass

    @abstractmethod
    def add_message_to_chat(self, chat_id: int, role: str, message: str) -> None:
        pass

    @abstractmethod
    def get_chat_history(self, chat_id: int) -> list[dict]:
        pass

    @abstractmethod
    def get_all_chats(self) -> Dict:
        pass

    @abstractmethod
    def remove_chat(self, id: str) -> None:
        pass

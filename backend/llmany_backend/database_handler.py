from typing import Tuple, Dict
from abc import ABC, abstractmethod


class DatabaseHandler(ABC):
    @abstractmethod
    def get_model_for_chat(self, id: str) -> Tuple[str, str]:
        return ...

    @abstractmethod
    def create_new_chat(self) -> str:
        return ...

    @abstractmethod
    def add_message_to_chat(self, id: str, message: str) -> None:
        pass

    @abstractmethod
    def get_chat_history(self, id: str) -> Dict:
        return ...

    @abstractmethod
    def get_all_chats(self) -> Dict:
        return ...

    @abstractmethod
    def remove_chat(self, id: str) -> None:
        pass

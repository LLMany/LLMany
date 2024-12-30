from abc import ABC, abstractmethod


class DatabaseError(Exception):
    """Base exception for database-related errors."""

    pass


class DatabaseHandler(ABC):
    @abstractmethod
    def get_model_for_chat(self, id: str) -> dict[str, str]:
        pass

    @abstractmethod
    def create_new_chat(self, model_type: str, model: str) -> int:
        pass

    @abstractmethod
    def add_message_to_chat(self, chat_id: int, role: str, message: str) -> None:
        pass

    @abstractmethod
    def get_chat_history(self, chat_id: int) -> list[dict[str, str]]:
        pass

    @abstractmethod
    def get_all_chats(self) -> list[dict[str, str]]:
        pass

    @abstractmethod
    def remove_chat(self, chat_id: int) -> None:
        pass

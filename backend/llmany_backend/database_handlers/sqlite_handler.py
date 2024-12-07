from typing import Tuple, Dict

from llmany_backend.database_handler import DatabaseHandler


class SQLiteHandler(DatabaseHandler):
    def __init__(self, connection=None) -> None:
        self.connection = connection

    def get_model_for_chat(self, id: str) -> Tuple[str, str]:
        return ...

    def create_new_chat(self) -> str:
        return ...

    def add_message_to_chat(self, id: str, message: str) -> None:
        pass

    def get_chat_history(self, id: str) -> Dict:
        return ...

    def get_all_chats(self) -> Dict:
        return ...

    def remove_chat(self, id: str) -> None:
        pass

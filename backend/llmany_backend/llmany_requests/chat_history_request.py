import json
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request


class ChatHistoryRequest(Request):
    def __init__(self, database_handler: DatabaseHandler, chat_ID: int) -> None:
        self.database_handler: DatabaseHandler = database_handler
        self.chat_ID: int = chat_ID

    @classmethod
    def from_dict(cls, request: dict, database_handler: DatabaseHandler):
        return cls(database_handler, request["chat_id"])

    def execute(self) -> None:
        chat_history: list[dict[str, str]] = self.database_handler.get_chat_history(
            self.chat_ID
        )
        returned_value = {
            "type": "chat_history",
            "chat_id": self.chat_ID,
            "messages": chat_history,
        }
        print(json.dumps(returned_value))

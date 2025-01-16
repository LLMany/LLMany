import json
import sqlite3
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.llmany_request import LLManyRequest


class DeleteChatRequest(LLManyRequest):
    def __init__(self, database_handler: DatabaseHandler, chat_ID: int) -> None:
        self.database_handler: DatabaseHandler = database_handler
        self.chat_ID: int = chat_ID

    @classmethod
    def from_dict(cls, request: dict, database_handler: DatabaseHandler):
        return cls(database_handler, request["chat_id"])

    def execute(self) -> None:
        try:
            self.database_handler.remove_chat(self.chat_ID)
        except sqlite3.Error:
            status = False
        else:
            status = True
        returned_value = {
            "type": "delete_chat",
            "chat_id": self.chat_ID,
            "status": status,
        }
        print(json.dumps(returned_value), flush=True)

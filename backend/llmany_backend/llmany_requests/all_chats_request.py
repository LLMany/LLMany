import json
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request


class AllChatsRequest(Request):
    def __init__(self, database_handler: DatabaseHandler) -> None:
        self.database_handler: DatabaseHandler = database_handler

    @classmethod
    def from_dict(cls, request: dict, database_handler: DatabaseHandler):
        return cls(database_handler)

    def execute(self) -> None:
        all_chats: list[dict[str, str]] = self.database_handler.get_all_chats()
        returned_value = {"type": "all_chats", "chats": all_chats}
        print(json.dumps(returned_value), flush=True)

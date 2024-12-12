from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request


class AllChatsRequest(Request):
    def __init__(self, database_handler: DatabaseHandler) -> None:
        self.database_handler: DatabaseHandler = database_handler

    @classmethod
    def from_dict(cls, request: dict, database_handler: DatabaseHandler):
        raise NotImplementedError

    def execute(self) -> str:
        raise NotImplementedError

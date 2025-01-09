from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request


class RemoveApiKeyRequest(Request):
    def __init__(self, database_handler: DatabaseHandler, model_type: str) -> None:
        self.database_handler: DatabaseHandler = database_handler
        self.model_type: str = model_type

    @classmethod
    def from_dict(cls, request: dict, database_handler: DatabaseHandler):
        return cls(database_handler, request["model_type"])

    def execute(self) -> None:
        self.database_handler.remove_api_key(self.model_type)

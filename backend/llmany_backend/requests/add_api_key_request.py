from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request


class AddApiKeyRequest(Request):
    def __init__(
        self, database_handler: DatabaseHandler, model_type: str, api_key: str
    ) -> None:
        self.database_handler: DatabaseHandler = database_handler
        self.model_type: str = model_type
        self.api_key: str = api_key

    @classmethod
    def from_dict(cls, request: dict, database_handler: DatabaseHandler):
        return cls(database_handler, request["model_type"], request["api_key"])

    def execute(self) -> None:
        self.database_handler.add_api_key(self.model_type, self.api_key)

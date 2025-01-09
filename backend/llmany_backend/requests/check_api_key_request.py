from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request


class CheckApiKeyRequest(Request):
    def __init__(
        self, database_handler: DatabaseHandler, model_type: str, api_key: str
    ) -> None:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, request: dict, database_handler: DatabaseHandler):
        raise NotImplementedError

    def execute(self) -> None:
        raise NotImplementedError

import json
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.llmany_request import Request


class CheckApiKeyRequest(Request):
    def __init__(self, database_handler: DatabaseHandler, model_type: str) -> None:
        self.database_handler: DatabaseHandler = database_handler
        self.model_type: str = model_type

    @classmethod
    def from_dict(cls, request: dict, database_handler: DatabaseHandler):
        return cls(database_handler, request["model_type"])

    def execute(self) -> None:
        exists: bool
        if self.database_handler.get_api_key(self.model_type) is None:
            exists = False
        else:
            exists = True

        returned_value = {
            "type": "check_api_key",
            "chat_id": self.model_type,
            "exists": exists,
        }
        print(json.dumps(returned_value))

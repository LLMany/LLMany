from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.llmany_request import LLManyRequest
import json


class NewChatRequest(LLManyRequest):
    def __init__(
        self, database_handler: DatabaseHandler, model_type: str, model: str
    ) -> None:
        self.database_handler: DatabaseHandler = database_handler
        self.model_type: str = model_type
        self.model: str = model

    @classmethod
    def from_dict(cls, request: dict, database_handler: DatabaseHandler):
        return cls(database_handler, request["model_type"], request["model"])

    def execute(self) -> None:
        new_chat_ID: int = self.database_handler.create_new_chat(
            self.model_type, self.model
        )
        returned_value = {
            "type": "new_chat",
            "model_type": self.model_type,
            "model": self.model,
            "chat_id": new_chat_ID,
        }
        print(json.dumps(returned_value), flush=True)

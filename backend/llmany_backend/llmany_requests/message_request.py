from llmany_backend.model_handler import ModelHandler
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.llmany_request import LLManyRequest
import json


class MessageRequest(LLManyRequest):
    def __init__(
        self,
        database_handler: DatabaseHandler,
        model_type: str,
        model: str,
        chat_ID: int,
        chat_history: list[dict[str, str]],
        contents: str,
    ) -> None:
        self.database_handler: DatabaseHandler = database_handler
        self.model_type: str = model_type
        self.model: str = model
        self.chat_ID: int = chat_ID
        self.chat_history: list[dict[str, str]] = chat_history
        self.contents: str = contents

    @classmethod
    def from_dict(
        cls,
        request: dict,
        database_handler: DatabaseHandler,
    ):
        model_info: dict[str, str] = database_handler.get_model_for_chat(
            request["chat_id"]
        )
        chat_history = database_handler.get_chat_history(request["chat_id"])

        return cls(
            database_handler,
            model_info["model_type"],
            model_info["model"],
            request["chat_id"],
            chat_history,
            request["contents"],
        )

    def execute(self) -> None:
        api_key = self.database_handler.get_api_key(self.model_type)
        if self.model_type == "HuggingFace":
            api_key = ""
        if api_key is None:
            returned_value = {
                "type": "message",
                "chat_id": self.chat_ID,
                "content": f"No API key provided for the model type: {self.model_type}",
            }
        else:
            model: ModelHandler = ModelHandlerFactory.create_model_handler(
                self.model_type, api_key
            )
            response: str = model.send_message(
                model=self.model, message=self.contents, history=self.chat_history
            )
            self.database_handler.add_message_to_chat(
                self.chat_ID, "user", self.contents
            )
            self.database_handler.add_message_to_chat(
                self.chat_ID, "assistant", response
            )
            returned_value = {
                "type": "message",
                "chat_id": self.chat_ID,
                "content": response,
            }
        print(json.dumps(returned_value), flush=True)

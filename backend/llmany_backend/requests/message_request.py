from llmany_backend.model_handler import ModelHandler
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.request import Request
import json


class MessageRequest(Request):
    def __init__(
        self,
        model_handler: ModelHandlerFactory,
        database_handler: DatabaseHandler,
        model_type: str,
        model: str,
        chat_ID: int,
        chat_history: list[dict[str, str]],
        contents: str,
    ) -> None:
        self.model_handler: ModelHandlerFactory = model_handler
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
        model_handler_factory: ModelHandlerFactory,
    ):
        model_info: dict[str, str] = database_handler.get_model_for_chat(
            request["chat_id"]
        )
        chat_history = database_handler.get_chat_history(request["chat_id"])

        return cls(
            model_handler_factory,
            database_handler,
            model_info["model_type"],
            model_info["model"],
            request["chat_id"],
            chat_history,
            request["contents"],
        )

    def execute(self) -> None:
        model: ModelHandler = self.model_handler.create_model_handler(self.model_type)
        self.chat_history.append({"role": "user", "content": self.contents})
        response: str = model.send_message(model=self.model, messages=self.chat_history)
        self.database_handler.add_message_to_chat(self.chat_ID, "user", self.contents)
        self.database_handler.add_message_to_chat(self.chat_ID, "assistant", response)
        returned_value = {
            "type": "message",
            "chat_id": self.chat_ID,
            "content": response,
        }
        print(json.dumps(returned_value))

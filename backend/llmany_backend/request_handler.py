import json

from llmany_backend.database_handler_factory import DatabaseHandlerFactory
from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.request import Request
from llmany_backend.requests import (
    AllChatsRequest,
    ChatHistoryRequest,
    DeleteChatRequest,
    NewChatRequest,
    MessageRequest,
)


class RequestHandler:
    def __init__(
        self,
        database_handler_factory: DatabaseHandlerFactory,
        model_handler_factory: ModelHandlerFactory,
    ) -> None:
        self.database_handler_factory: DatabaseHandlerFactory = database_handler_factory
        self.model_handler_factory: ModelHandlerFactory = model_handler_factory

    def parse(self) -> dict:
        request_json = input()
        return json.loads(request_json)

    def create_request(self, request_data: dict) -> Request:
        match request_data["type"]:
            case "AllChatsRequest":
                return AllChatsRequest()
            case "ChatHistoryRequest":
                return ChatHistoryRequest(request_data["chat_id"])
            case "DeleteChatRequest":
                return DeleteChatRequest(request_data["chat_id"])
            case "NewChatRequest":
                return NewChatRequest()
            case "MessageRequest":
                return MessageRequest(request_data["message"])
            case _:
                raise ValueError("Invalid request type")

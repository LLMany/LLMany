import json
from sqlite3 import Connection

from llmany_backend.database_handler_factory import DatabaseHandlerFactory
from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.llmany_request import LLManyRequest
from llmany_backend.llmany_requests import (
    AllChatsRequest,
    ChatHistoryRequest,
    DeleteChatRequest,
    NewChatRequest,
    MessageRequest,
    AddApiKeyRequest,
    RemoveApiKeyRequest,
    CheckApiKeyRequest,
)


class RequestHandler:
    def __init__(
        self,
        database_handler_factory: DatabaseHandlerFactory,
        model_handler_factory: ModelHandlerFactory,
        connection: Connection,
    ) -> None:
        self.database_handler_factory: DatabaseHandlerFactory = database_handler_factory
        self.model_handler_factory: ModelHandlerFactory = model_handler_factory
        self.connection = connection
        self.database_handler = self.database_handler_factory.create_database_handler(
            "SQLite3", self.connection
        )

    def parse(self, request_json: str) -> dict:
        return json.loads(request_json)

    def create_request(self, request_data: dict) -> LLManyRequest:
        match request_data["type"]:
            case "all_chats":
                return AllChatsRequest.from_dict(request_data, self.database_handler)
            case "chat_history":
                return ChatHistoryRequest.from_dict(request_data, self.database_handler)
            case "delete_chat":
                return DeleteChatRequest.from_dict(request_data, self.database_handler)
            case "new_chat":
                return NewChatRequest.from_dict(request_data, self.database_handler)
            case "message":
                return MessageRequest.from_dict(
                    request_data,
                    self.database_handler,
                    self.model_handler_factory,
                )
            case "add_api_key":
                return AddApiKeyRequest.from_dict(request_data, self.database_handler)
            case "remove_api_key":
                return RemoveApiKeyRequest.from_dict(
                    request_data, self.database_handler
                )
            case "check_api_key":
                return CheckApiKeyRequest.from_dict(request_data, self.database_handler)
            case _:
                raise ValueError("Invalid request type")

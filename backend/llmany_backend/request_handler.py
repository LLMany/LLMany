import json
from sqlite3 import Connection

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
        connection: Connection,
    ) -> None:
        self.database_handler_factory: DatabaseHandlerFactory = database_handler_factory
        self.model_handler_factory: ModelHandlerFactory = model_handler_factory
        self.connection = connection

    def parse(self) -> dict:
        request_json = input()
        return json.loads(request_json)

    def create_request(self, request_data: dict) -> Request:
        match request_data["type"]:
            case "AllChatsRequest":
                return AllChatsRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        "SQLite", self.connection
                    ),
                )
            case "ChatHistoryRequest":
                return ChatHistoryRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        "SQLite", self.connection
                    ),
                )
            case "DeleteChatRequest":
                return DeleteChatRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        "SQLite", self.connection
                    ),
                )
            case "NewChatRequest":
                return NewChatRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        "SQLite", self.connection
                    ),
                )
            case "MessageRequest":
                return MessageRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        "SQLite", self.connection
                    ),
                    self.model_handler_factory,
                )
            case _:
                raise ValueError("Invalid request type")

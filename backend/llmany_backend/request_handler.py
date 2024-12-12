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

    def parse(self, request_json: str) -> dict:
        return json.loads(request_json)

    def create_request(self, request_data: dict) -> Request:
        database = "SQLite3"
        match request_data["type"]:
            case "all_chats":
                return AllChatsRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        database, self.connection
                    ),
                )
            case "chat_history":
                return ChatHistoryRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        database, self.connection
                    ),
                )
            case "delete_chat":
                return DeleteChatRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        database, self.connection
                    ),
                )
            case "new_chat":
                return NewChatRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        database, self.connection
                    ),
                )
            case "message":
                return MessageRequest.from_dict(
                    request_data,
                    self.database_handler_factory.create_database_handler(
                        database, self.connection
                    ),
                    self.model_handler_factory,
                )
            case _:
                raise ValueError("Invalid request type")

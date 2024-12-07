from llmany_backend.database_handler_factory import DatabaseHandlerFactory
from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.request import Request


class RequestHandler:
    def __init__(
        self,
        database_handler_factory: "DatabaseHandlerFactory",
        model_handler_factory: "ModelHandlerFactory",
    ) -> None:
        self.database_handler_factory: DatabaseHandlerFactory = database_handler_factory
        self.model_handler_factory: ModelHandlerFactory = model_handler_factory

    def parse(self) -> dict:
        return ...
    
    def create_request(self, request_data :dict) -> Request:
        return ...

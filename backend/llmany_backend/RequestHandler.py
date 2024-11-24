
from llmany_backend.DatabaseHandlerFactory import DatabaseHandlerFactory
from llmany_backend.ModelHandlerFactory import ModelHandlerFactory
from llmany_backend.Request import Request


class RequestHandler:
    def __init__(self, database_handler_factory: 'DatabaseHandlerFactory', 
                 model_handler_factory: 'ModelHandlerFactory') -> None:
        self.database_handler_factory: DatabaseHandlerFactory = database_handler_factory
        self.model_handler_factory: ModelHandlerFactory = model_handler_factory

    def parse(self) -> Request:
        return ...

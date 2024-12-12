from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request


class NewChatRequest(Request):
    def __init__(
        self, database_handler: "DatabaseHandler", model_type: str, model: str
    ) -> None:
        self.database_handler: DatabaseHandler = database_handler
        self.model_type: str = model_type
        self.model: str = model

    def execute(self) -> str:
        raise NotImplementedError

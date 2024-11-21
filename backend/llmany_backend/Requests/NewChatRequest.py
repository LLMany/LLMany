from LLMany.backend.llmany_backend.DatabaseHandler import DatabaseHandler
from LLMany.backend.llmany_backend.Request import Request

class NewChatRequest(Request):
    def __init__(self, database_handler: 'DatabaseHandler', model_type: str, model: str) -> None:
        self.database_handler: DatabaseHandler = database_handler 
        self.model_type: str = model_type 
        self.model: str = model

    def execute(self) -> str:
        return ... 
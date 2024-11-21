from LLMany.backend.llmany_backend.DatabaseHandler import DatabaseHandler
from LLMany.backend.llmany_backend.Request import Request

class AllChatRequest(Request):
    def __init__(self, database_handler: 'DatabaseHandler') -> None:
        self.database_handler: DatabaseHandler = database_handler 

    def execute(self) -> str:
        return ... 
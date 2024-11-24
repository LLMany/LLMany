from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request

class AllChatRequest(Request):
    def __init__(self, database_handler: 'DatabaseHandler') -> None:
        self.database_handler: DatabaseHandler = database_handler 

    def execute(self) -> str:
        return ... 
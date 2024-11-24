from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request

class DeleteChatRequest(Request):
    def __init__(self, database_handler: 'DatabaseHandler', chat_ID: str) -> None:
        self.database_handler: DatabaseHandler = database_handler  
        self.chat_ID: str = chat_ID  

    def execute(self) -> str:
        return ... 
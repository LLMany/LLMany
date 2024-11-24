from llmany_backend.DatabaseHandler import DatabaseHandler
from llmany_backend.ModelHandlerFactory import ModelHandlerFactory
from llmany_backend.Request import Request

class MessageRequest(Request):
    def __init__(self, 
                 model_handler: 'ModelHandlerFactory', 
                 database_handler: 'DatabaseHandler', 
                 model_type: str, 
                 model: str, 
                 chat_ID: str, 
                 chat_history: str) -> None:
        self.model_handler: ModelHandlerFactory = model_handler  
        self.database_handler: DatabaseHandler = database_handler  
        self.model_type: str = model_type  
        self.model: str = model  
        self.chat_ID: str = chat_ID  
        self.chat_history: str = chat_history
    
    def execute(self) -> str:
        return ...
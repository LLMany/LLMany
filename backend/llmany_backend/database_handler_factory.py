from llmany_backend.database_handler import DatabaseHandler


class DatabaseHandlerFactory:
    def create_database_handler(self, model_type: str) -> DatabaseHandler:
        return ...
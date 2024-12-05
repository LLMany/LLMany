from llmany_backend.database_handler import DatabaseHandler


class DatabaseHandlerFactory:
    def create_database_handler(self, database: str) -> DatabaseHandler:
        return ...

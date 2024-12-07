import sqlite3

from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.database_handlers import SQLiteHandler


class DatabaseHandlerFactory:
    def create_database_handler(
        self, database: str, connection: sqlite3.Connection
    ) -> DatabaseHandler:
        match database:
            case "SQLite3":
                return SQLiteHandler(connection)
            case _:
                raise TypeError("Database not supported")

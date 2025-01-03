import pytest
import sqlite3

from llmany_backend.database_handler_factory import DatabaseHandlerFactory
from llmany_backend.database_handlers.sqlite_handler import SQLiteHandler


@pytest.mark.parametrize(
    "database_type, database_handler_class",
    [
        ("SQLite3", SQLiteHandler),
    ],
)
def test_proper_handler_created(database_type, temp_file, database_handler_class):
    connection = sqlite3.connect(temp_file)
    factory = DatabaseHandlerFactory()
    handler = factory.create_database_handler(database_type, connection)
    assert isinstance(handler, database_handler_class)

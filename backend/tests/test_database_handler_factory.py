import pytest

from llmany_backend.database_handler_factory import DatabaseHandlerFactory
from llmany_backend.database_handlers import SQLiteHandler


@pytest.mark.parametrize(
        "database_type, database_handler_class",
        [("SQLite", SQLiteHandler),
         ]
)
def test_proper_handler_created(database_type, database_handler_class):
    factory = DatabaseHandlerFactory()
    handler = factory.create_database_handler(database_type)
    assert isinstance(handler, database_handler_class)
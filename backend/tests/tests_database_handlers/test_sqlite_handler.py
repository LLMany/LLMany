import sqlite3
import os
import pytest
import tempfile
from unittest.mock import MagicMock

from llmany_backend.database_handlers.sqlite_handler import SQLiteHandler


@pytest.fixture
def temp_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_name = temp_file.name
    yield temp_file_name
    # Cleanup after test
    if os.path.exists(temp_file_name):
        os.remove(temp_file_name)


@pytest.mark.parametrize(
    "chat_id, model_type, model",
    [
        (1, "OpenAI", "gpt-4o"),
        (2, "Anthropic", "claude-3.5"),
        (3, "OpenAI", "gpt-4"),
        (4, "Anthropic", "claude-2.5"),
        (5, "Google", "Gemini 1.5"),
    ],
)
def test_get_model_for_chat(chat_id, model_type, model, temp_file):
    connection = sqlite3.connect(temp_file)
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER PRIMARY KEY, name TEXT, model_type TEXT, model TEXT)"
    )
    connection.commit()

    cursor.execute(
        "INSERT INTO chats (chat_id, name, model_type, model) VALUES (?, ?, ?, ?)",
        (chat_id, "Test Chat", model_type, model),
    )
    cursor.commit()

    handler = SQLiteHandler(connection)
    result = handler.get_model_for_chat(chat_id)

    assert isinstance(result, tuple)
    returned_model_type, returned_model = result

    assert returned_model_type == model_type
    assert returned_model == model

    cursor.close()
    connection.close()


@pytest.mark.parametrize(
    "model_list",
    [
        [("OpenAI", "gpt-4o")],
        [("Anthropic", "claude-3.5"), ("OpenAI", "gpt-4")],
        [
            ("Anthropic", "claude-2.5"),
            ("Google", "Gemini 1.5"),
            ("Google, Gemini 1.5 "),
        ],
    ],
)
def test_create_new_chat(model_list, temp_file):
    connection = sqlite3.connect(temp_file)
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER PRIMARY KEY, name TEXT, model_type TEXT, model TEXT)"
    )
    connection.commit()
    cursor.close()

    for entry in model_list:
        model_type, model = entry
        handler = SQLiteHandler(connection)
        chat_id = handler.create_new_chat(model_type, model)

        result = handler.get_model_for_chat(chat_id)

        assert isinstance(chat_id, int)

        returned_model_type, returned_model = result

        assert returned_model_type == model_type
        assert returned_model == model

    connection.close()


def test_sqlite_handler_initialization():
    mock_connection = MagicMock()

    handler = SQLiteHandler(mock_connection)

    assert handler.connection == mock_connection


def test_get_model_for_chat_mocked():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)

    mock_connection.execute.return_value = [("gpt-4", "chat-12345")]

    result = handler.get_model_for_chat("chat-12345")

    assert result == ("gpt-4", "chat-12345")
    mock_connection.execute.assert_called_once_with(
        "SELECT model, chat_id FROM chats WHERE chat_id = ?", ("chat-12345",)
    )


def test_create_new_chat_mocked():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)

    mock_connection.execute.return_value = "new_chat_id"

    result = handler.create_new_chat()

    assert result == "new_chat_id"
    mock_connection.execute.assert_called_once_with(
        "INSERT INTO chats (model, chat_id) VALUES (?, ?)",
        ("default_model", "new_chat_id"),
    )


def test_add_message_to_chat():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)

    handler.add_message_to_chat("chat-12345", "Hello, world!")

    mock_connection.execute.assert_called_once_with(
        "INSERT INTO messages (chat_id, message) VALUES (?, ?)",
        ("chat-12345", "Hello, world!"),
    )


def test_get_chat_history():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)

    mock_connection.execute.return_value = [
        {"message": "Hello, world!", "timestamp": "2024-11-29"}
    ]

    result = handler.get_chat_history("chat-12345")

    assert result == [{"message": "Hello, world!", "timestamp": "2024-11-29"}]
    mock_connection.execute.assert_called_once_with(
        "SELECT message, timestamp FROM messages WHERE chat_id = ?", ("chat-12345",)
    )


def test_get_all_chats():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)

    mock_connection.execute.return_value = [{"chat_id": "chat-12345", "model": "gpt-4"}]

    result = handler.get_all_chats()

    assert result == [{"chat_id": "chat-12345", "model": "gpt-4"}]
    mock_connection.execute.assert_called_once_with("SELECT chat_id, model FROM chats")


def test_remove_chat():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)

    handler.remove_chat("chat-12345")

    mock_connection.execute.assert_called_once_with(
        "DELETE FROM chats WHERE chat_id = ?", ("chat-12345",)
    )

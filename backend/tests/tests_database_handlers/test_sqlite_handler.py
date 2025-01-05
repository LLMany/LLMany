import sqlite3
import pytest
from unittest.mock import MagicMock, patch

from llmany_backend.database_handlers.sqlite_handler import SQLiteHandler


@pytest.mark.parametrize(
    "model_type, model",
    [
        ("OpenAI", "gpt-4o"),
        ("Anthropic", "claude-3.5"),
        ("OpenAI", "gpt-4"),
        ("Anthropic", "claude-2.5"),
        ("Google", "Gemini 1.5"),
    ],
)
def test_get_model_for_chat(model_type, model, temp_file):
    connection = sqlite3.connect(temp_file)
    cursor = connection.cursor()
    handler = SQLiteHandler(connection)

    cursor.execute(
        "INSERT INTO chats (name, model_type, model) VALUES (?, ?, ?)",
        ("Test Chat", model_type, model),
    )

    chat_id = cursor.lastrowid
    connection.commit()

    result = handler.get_model_for_chat(chat_id)

    assert isinstance(result, dict)

    returned_model_type = result["model_type"]
    returned_model = result["model"]

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
            ("Google", "Gemini 1.5 "),
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

        returned_model_type = result["model_type"]
        returned_model = result["model"]

        assert returned_model_type == model_type
        assert returned_model == model

    connection.close()


def test_sqlite_handler_initialization():
    mock_connection = MagicMock()
    with patch.object(SQLiteHandler, "ensure_tables_exist", return_value=None):
        handler = SQLiteHandler(mock_connection)
        assert handler.connection == mock_connection
    mock_connection.cursor().execute.assert_not_called()


def test_get_model_for_chat_mocked():
    mock_connection = MagicMock()
    with patch.object(SQLiteHandler, "ensure_tables_exist", return_value=None):
        handler = SQLiteHandler(mock_connection)

    mock_connection.cursor().fetchone.return_value = ("OpenAI", "gpt-4")

    result = handler.get_model_for_chat(123)

    assert result == {"model_type": "OpenAI", "model": "gpt-4"}
    mock_connection.cursor().execute.assert_called_once_with(
        "SELECT model_type, model FROM chats WHERE chat_id = ?", (123,)
    )


def test_create_new_chat_mocked():
    mock_connection = MagicMock()
    with patch.object(SQLiteHandler, "ensure_tables_exist", return_value=None):
        handler = SQLiteHandler(mock_connection)

    mock_connection.cursor().lastrowid = 42

    result = handler.create_new_chat("OpenAI", "gpt-4")

    assert result == 42
    mock_connection.cursor().execute.assert_called_once_with(
        "INSERT INTO chats (name, model_type, model) VALUES (?, ?, ?)",
        ("Test Chat", "OpenAI", "gpt-4"),
    )


def test_add_message_to_chat():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)

    mock_cursor = mock_connection.cursor.return_value
    mock_cursor.fetchone.return_value = (5,)

    handler.add_message_to_chat(1, "user", "Hello, world!")

    mock_cursor.execute.assert_any_call(
        "SELECT MAX(message_id) AS max_id FROM messages WHERE chat_id = ?",
        (1,),
    )
    mock_cursor.execute.assert_any_call(
        "INSERT INTO messages (chat_id, message_id, role, message) VALUES (?, ?, ?, ?)",
        (1, 6, "user", "Hello, world!"),
    )
    mock_connection.commit.assert_called_once()


def test_get_chat_history():
    mock_connection = MagicMock()
    with patch.object(SQLiteHandler, "ensure_tables_exist", return_value=None):
        handler = SQLiteHandler(mock_connection)

    mock_connection.cursor().fetchall.return_value = [("user", "Hello!")]

    result = handler.get_chat_history(123)

    assert result == [{"role": "user", "content": "Hello!"}]
    mock_connection.cursor().execute.assert_called_once_with(
        "SELECT role, message FROM messages WHERE chat_id = ? ORDER BY message_id",
        (123,),
    )


def test_get_all_chats():
    mock_connection = MagicMock()
    with patch.object(SQLiteHandler, "ensure_tables_exist", return_value=None):
        handler = SQLiteHandler(mock_connection)

    mock_connection.cursor().fetchall.return_value = [
        (1, "OpenAI", "gpt-4"),
        (2, "Anthropic", "claude-2"),
    ]

    result = handler.get_all_chats()

    assert result == [
        {"chat_id": 1, "model_type": "OpenAI", "model": "gpt-4"},
        {"chat_id": 2, "model_type": "Anthropic", "model": "claude-2"},
    ]
    mock_connection.cursor().execute.assert_called_once_with(
        "SELECT chat_id, model_type, model FROM chats"
    )


def test_remove_chat():
    mock_connection = MagicMock()
    with patch.object(SQLiteHandler, "ensure_tables_exist", return_value=None):
        handler = SQLiteHandler(mock_connection)

    handler.remove_chat(123)

    mock_connection.cursor().execute.assert_called_once_with(
        "DELETE FROM chats WHERE chat_id = ?", (123,)
    )


def test_add_api_key(temp_file):
    conn = sqlite3.connect(temp_file)
    handler = SQLiteHandler(conn)
    handler.add_api_key("gpt-4", "your-api-key")

    assert handler.get_api_key("gpt-4") == "your-api-key"


def test_remove_api_key(temp_file):
    conn = sqlite3.connect(temp_file)
    handler = SQLiteHandler(conn)
    handler.add_api_key("gpt-4", "your-api-key")
    handler.remove_api_key("gpt-4")

    assert handler.get_api_key("gpt-4") is None

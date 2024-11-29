from unittest.mock import MagicMock
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.database_handlers.sqlite_handler import SQLiteHandler

def test_sqlite_handler_initialization():
    mock_connection = MagicMock()
    
    handler = SQLiteHandler(mock_connection)
    
    assert handler.connection == mock_connection

def test_get_model_for_chat():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)
    
    mock_connection.execute.return_value = [("gpt-4", "chat-12345")]
    
    result = handler.get_model_for_chat("chat-12345")
    
    assert result == ("gpt-4", "chat-12345")
    mock_connection.execute.assert_called_once_with("SELECT model, chat_id FROM chats WHERE chat_id = ?", ("chat-12345",))

def test_create_new_chat():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)
    
    mock_connection.execute.return_value = "new_chat_id"
    
    result = handler.create_new_chat()
    
    assert result == "new_chat_id"
    mock_connection.execute.assert_called_once_with("INSERT INTO chats (model, chat_id) VALUES (?, ?)", ("default_model", "new_chat_id"))

def test_add_message_to_chat():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)
    
    handler.add_message_to_chat("chat-12345", "Hello, world!")
    
    mock_connection.execute.assert_called_once_with("INSERT INTO messages (chat_id, message) VALUES (?, ?)", ("chat-12345", "Hello, world!"))

def test_get_chat_history():
    mock_connection = MagicMock()
    handler = SQLiteHandler(mock_connection)
    
    mock_connection.execute.return_value = [{"message": "Hello, world!", "timestamp": "2024-11-29"}]
    
    result = handler.get_chat_history("chat-12345")
    
    assert result == [{"message": "Hello, world!", "timestamp": "2024-11-29"}]
    mock_connection.execute.assert_called_once_with("SELECT message, timestamp FROM messages WHERE chat_id = ?", ("chat-12345",))

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
    
    mock_connection.execute.assert_called_once_with("DELETE FROM chats WHERE chat_id = ?", ("chat-12345",))


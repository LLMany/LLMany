from unittest.mock import MagicMock
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.requests.delete_chat_request import DeleteChatRequest

def test_delete_chat_request_initialization():
    mock_database_handler = MagicMock(DatabaseHandler)
    chat_id = "12345"
    
    request = DeleteChatRequest(mock_database_handler, chat_id)
    
    assert request.database_handler == mock_database_handler
    assert request.chat_ID == chat_id

def test_execute_delete_chat_request(mocker):
    mock_database_handler = MagicMock(DatabaseHandler)
    
    mock_database_handler.delete_chat.return_value = "Chat deleted successfully"
    
    chat_id = "12345"
    request = DeleteChatRequest(mock_database_handler, chat_id)
    
    result = request.execute()
    
    assert result == "Chat deleted successfully"
    
    mock_database_handler.delete_chat.assert_called_once_with(chat_id)

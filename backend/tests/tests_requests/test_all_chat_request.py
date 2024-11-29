from unittest.mock import MagicMock
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.requests.all_chat_request import AllChatRequest

def test_all_chat_request_initialization():
    mock_database_handler = MagicMock(DatabaseHandler)
    
    request = AllChatRequest(mock_database_handler)
    
    assert request.database_handler == mock_database_handler

def test_execute_all_chat_request(mocker):
    mock_database_handler = MagicMock(DatabaseHandler)
    
    mock_database_handler.get_all_chats.return_value = ["Chat 1", "Chat 2", "Chat 3"]
    
    request = AllChatRequest(mock_database_handler)
    
    result = request.execute()
    
    assert result == ["Chat 1", "Chat 2", "Chat 3"]
    
    mock_database_handler.get_all_chats.assert_called_once()


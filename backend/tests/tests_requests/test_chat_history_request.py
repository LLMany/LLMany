from unittest import mock
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.request import Request
from llmany_backend.requests.chat_history_request import ChatHistoryRequest 

def test_chat_history_request_initialization(mocker):
    mock_database_handler = mocker.Mock(spec=DatabaseHandler)
    
    chat_id = "12345"
    request = ChatHistoryRequest(mock_database_handler, chat_id)

    assert request.database_handler == mock_database_handler
    assert request.chat_ID == chat_id

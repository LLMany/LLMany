from unittest.mock import MagicMock
from llmany_backend.requests.new_chat_request import NewChatRequest
from llmany_backend.database_handler import DatabaseHandler

def test_new_chat_request_init():
    mock_database_handler = MagicMock(DatabaseHandler)
    
    request = NewChatRequest(
        database_handler=mock_database_handler,
        model_type="gpt-3",
        model="gpt-4"
    )

    assert request.database_handler == mock_database_handler
    assert request.model_type == "gpt-3"
    assert request.model == "gpt-4"

def test_execute_new_chat_request(mocker):
    mock_database_handler = MagicMock(DatabaseHandler)

    request = NewChatRequest(
        database_handler=mock_database_handler,
        model_type="gpt-3",
        model="gpt-4"
    )

    mock_execute = mocker.patch.object(request, "execute", return_value="chat created")
    
    result = request.execute()

    assert result == "chat created"
    
    mock_database_handler.save.assert_called_once()

import builtins
from unittest.mock import MagicMock
from llmany_backend.llmany_requests import NewChatRequest
from llmany_backend.database_handler import DatabaseHandler
import json


def test_new_chat_request_init():
    mock_database_handler = MagicMock(DatabaseHandler)

    request = NewChatRequest(
        database_handler=mock_database_handler, model_type="gpt-3", model="openai"
    )

    assert request.database_handler == mock_database_handler
    assert request.model_type == "gpt-3"
    assert request.model == "openai"


def test_new_chat_request_from_dict():
    mock_database_handler = MagicMock(DatabaseHandler)
    request_data = {"model_type": "gpt-4", "model": "openai"}

    request = NewChatRequest.from_dict(request_data, mock_database_handler)

    assert request.database_handler == mock_database_handler
    assert request.model_type == "gpt-4"
    assert request.model == "openai"


def test_execute_new_chat_request(mocker):
    mock_database_handler = MagicMock(DatabaseHandler)

    mock_database_handler.create_new_chat.return_value = 123

    request = NewChatRequest(
        database_handler=mock_database_handler, model_type="gpt-3", model="openai"
    )

    mocker.patch("builtins.print")

    request.execute()

    mock_database_handler.create_new_chat.assert_called_once_with("gpt-3", "openai")

    expected_output = {
        "type": "new_chat",
        "model_type": "gpt-3",
        "model": "openai",
        "chat_id": 123,
    }

    builtins.print.assert_called_once_with(json.dumps(expected_output))

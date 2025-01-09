from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.llmany_requests.remove_api_key_request import RemoveApiKeyRequest
from unittest.mock import MagicMock


def test_remove_api_key_request_initialization():
    mock_database_handler = MagicMock(DatabaseHandler)

    model_type = "gpt-4"

    request = RemoveApiKeyRequest(mock_database_handler, model_type)

    assert request.database_handler == mock_database_handler
    assert request.model_type == model_type


def test_remove_api_key_request_from_dict():
    mock_database_handler = MagicMock(DatabaseHandler)

    request_data = {"model_type": "gpt-4"}

    request = RemoveApiKeyRequest.from_dict(request_data, mock_database_handler)

    assert request.database_handler == mock_database_handler
    assert request.model_type == "gpt-4"


def test_remove_api_key_request_execute():
    mock_database_handler = MagicMock(DatabaseHandler)

    model_type = "gpt-4"

    request = RemoveApiKeyRequest(mock_database_handler, model_type)

    request.execute()

    mock_database_handler.remove_api_key.assert_called_once_with(model_type)

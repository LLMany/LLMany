from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.llmany_requests.add_api_key_request import AddApiKeyRequest
from unittest.mock import MagicMock


def test_add_api_key_request_initialization():
    mock_database_handler = MagicMock(DatabaseHandler)
    model_type = "gpt-4"
    api_key = "test-api-key"

    request = AddApiKeyRequest(mock_database_handler, model_type, api_key)

    assert request.database_handler == mock_database_handler
    assert request.model_type == model_type
    assert request.api_key == api_key


def test_add_api_key_request_from_dict():
    mock_database_handler = MagicMock(DatabaseHandler)
    request_data = {
        "model_type": "gpt-4",
        "api_key": "test-api-key",
    }

    request = AddApiKeyRequest.from_dict(request_data, mock_database_handler)

    assert request.database_handler == mock_database_handler
    assert request.model_type == "gpt-4"
    assert request.api_key == "test-api-key"


def test_add_api_key_request_execute():
    mock_database_handler = MagicMock(DatabaseHandler)
    model_type = "gpt-4"
    api_key = "test-api-key"

    request = AddApiKeyRequest(mock_database_handler, model_type, api_key)

    request.execute()

    mock_database_handler.add_api_key.assert_called_once_with(model_type, api_key)

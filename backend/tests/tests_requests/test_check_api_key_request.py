from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.requests.check_api_key_request import CheckApiKeyRequest
from unittest.mock import MagicMock, patch
import json


def test_check_api_key_request_initialization():
    mock_database_handler = MagicMock(DatabaseHandler)
    model_type = "gpt-4"

    request = CheckApiKeyRequest(mock_database_handler, model_type)

    assert request.database_handler == mock_database_handler
    assert request.model_type == model_type


def test_check_api_key_request_from_dict():
    mock_database_handler = MagicMock(DatabaseHandler)
    request_data = {"model_type": "gpt-4"}

    request = CheckApiKeyRequest.from_dict(request_data, mock_database_handler)

    assert request.database_handler == mock_database_handler
    assert request.model_type == "gpt-4"


def test_check_api_key_request_execute_api_key_exists():
    mock_database_handler = MagicMock(DatabaseHandler)
    mock_database_handler.get_api_key.return_value = "some_api_key"
    model_type = "gpt-4"

    request = CheckApiKeyRequest(mock_database_handler, model_type)

    with patch("builtins.print") as mock_print:
        request.execute()

        mock_database_handler.get_api_key.assert_called_once_with(model_type)
        mock_print.assert_called_once_with(
            json.dumps(
                {
                    "type": "check_api_key",
                    "chat_id": model_type,
                    "exists": True,
                }
            )
        )


def test_check_api_key_request_execute_api_key_not_exists():
    mock_database_handler = MagicMock(DatabaseHandler)
    mock_database_handler.get_api_key.return_value = None
    model_type = "gpt-4"

    request = CheckApiKeyRequest(mock_database_handler, model_type)

    with patch("builtins.print") as mock_print:
        request.execute()

        mock_database_handler.get_api_key.assert_called_once_with(model_type)
        mock_print.assert_called_once_with(
            json.dumps(
                {
                    "type": "check_api_key",
                    "chat_id": model_type,
                    "exists": False,
                }
            )
        )

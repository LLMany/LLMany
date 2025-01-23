import json
from unittest.mock import MagicMock, patch
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.llmany_requests.all_chats_request import AllChatsRequest


def test_all_chats_request_initialization():
    mock_database_handler = MagicMock(DatabaseHandler)

    request = AllChatsRequest(mock_database_handler)

    assert request.database_handler == mock_database_handler


def test_all_chats_request_from_dict():
    mock_database_handler = MagicMock(DatabaseHandler)
    request_data = {}

    request = AllChatsRequest.from_dict(request_data, mock_database_handler)

    assert request.database_handler == mock_database_handler


def test_execute_all_chats_request():
    mock_database_handler = MagicMock(DatabaseHandler)

    mock_database_handler.get_all_chats.return_value = [
        {"model_type": "GPT-4", "model": "openai", "chat_id": 123},
        {"model_type": "GPT-3.5", "model": "openai", "chat_id": 456},
    ]

    request = AllChatsRequest(mock_database_handler)

    with patch("builtins.print") as mock_print:
        request.execute()

        expected_output = json.dumps(
            {
                "type": "all_chats",
                "chats": [
                    {"model_type": "GPT-4", "model": "openai", "chat_id": 123},
                    {"model_type": "GPT-3.5", "model": "openai", "chat_id": 456},
                ],
            }
        )

        mock_print.assert_called_once_with(expected_output, flush=True)

    mock_database_handler.get_all_chats.assert_called_once()

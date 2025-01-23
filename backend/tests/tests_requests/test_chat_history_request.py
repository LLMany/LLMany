import json
from unittest.mock import MagicMock, patch
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.llmany_requests.chat_history_request import ChatHistoryRequest


def test_chat_history_request_initialization():
    mock_database_handler = MagicMock(DatabaseHandler)

    chat_id = 12345
    request = ChatHistoryRequest(mock_database_handler, chat_id)

    assert request.database_handler == mock_database_handler
    assert request.chat_ID == chat_id


def test_chat_history_request_from_dict():
    mock_database_handler = MagicMock(DatabaseHandler)

    request_data = {"chat_id": 12345}
    request = ChatHistoryRequest.from_dict(request_data, mock_database_handler)

    assert request.database_handler == mock_database_handler
    assert request.chat_ID == 12345


def test_chat_history_request_execute():
    mock_database_handler = MagicMock(DatabaseHandler)

    chat_id = 12345
    chat_history = [
        {"role": "user", "content": "Hello there"},
        {"role": "assistant", "content": "General Kenobi"},
    ]

    mock_database_handler.get_chat_history.return_value = chat_history

    request = ChatHistoryRequest(mock_database_handler, chat_id)

    with patch("builtins.print") as mock_print:
        request.execute()

        expected_output = {
            "type": "chat_history",
            "chat_id": chat_id,
            "messages": chat_history,
        }

        mock_print.assert_called_once_with(json.dumps(expected_output), flush=True)

        mock_database_handler.get_chat_history.assert_called_once_with(chat_id)

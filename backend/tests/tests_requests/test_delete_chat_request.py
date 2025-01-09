import json
import sqlite3
from unittest.mock import MagicMock
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.llmany_requests.delete_chat_request import DeleteChatRequest


def test_delete_chat_request_initialization():
    mock_database_handler = MagicMock(spec=DatabaseHandler)
    chat_id = 12345

    request = DeleteChatRequest(mock_database_handler, chat_id)

    assert request.database_handler == mock_database_handler
    assert request.chat_ID == chat_id


def test_delete_chat_request_from_dict():
    mock_database_handler = MagicMock(spec=DatabaseHandler)
    request_dict = {"chat_id": 12345}

    request = DeleteChatRequest.from_dict(request_dict, mock_database_handler)

    assert request.database_handler == mock_database_handler
    assert request.chat_ID == 12345


def test_execute_delete_chat_request_success(mocker, capsys):
    mock_database_handler = mocker.Mock(spec=DatabaseHandler)

    chat_id = 12345
    mock_database_handler.remove_chat.return_value = True

    request = DeleteChatRequest(mock_database_handler, chat_id)

    request.execute()

    captured = capsys.readouterr()
    expected_output = {"type": "delete_chat", "chat_id": chat_id, "status": True}

    assert json.loads(captured.out) == expected_output
    mock_database_handler.remove_chat.assert_called_once_with(chat_id)


def test_execute_delete_chat_request_failure(mocker, capsys):
    mock_database_handler = mocker.Mock(spec=DatabaseHandler)

    chat_id = 12345
    mock_database_handler.remove_chat.side_effect = sqlite3.Error("Test error")

    request = DeleteChatRequest(mock_database_handler, chat_id)

    request.execute()

    captured = capsys.readouterr()
    expected_output = {"type": "delete_chat", "chat_id": chat_id, "status": False}

    assert json.loads(captured.out) == expected_output
    mock_database_handler.remove_chat.assert_called_once_with(chat_id)

import json
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.requests.chat_history_request import ChatHistoryRequest


def test_chat_history_request_initialization(mocker):
    mock_database_handler = mocker.Mock(spec=DatabaseHandler)

    chat_id = 12345
    request = ChatHistoryRequest(mock_database_handler, chat_id)

    assert request.database_handler == mock_database_handler
    assert request.chat_ID == chat_id


def test_chat_history_request_from_dict(mocker):
    mock_database_handler = mocker.Mock(spec=DatabaseHandler)

    request_dict = {"chat_id": 12345}
    request = ChatHistoryRequest.from_dict(request_dict, mock_database_handler)

    assert request.database_handler == mock_database_handler
    assert request.chat_ID == 12345


def test_execute_chat_history_request(mocker, capsys):
    mock_database_handler = mocker.Mock(spec=DatabaseHandler)

    chat_id = 12345
    chat_history_tuples = [("user", "Hello"), ("assistant", "Hi!")]

    mock_database_handler.get_chat_history.return_value = chat_history_tuples

    request = ChatHistoryRequest(mock_database_handler, chat_id)
    request.execute()

    captured = capsys.readouterr()
    expected_output = {
        "type": "chat_history",
        "chat_id": chat_id,
        "messages": [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi!"},
        ],
    }

    assert json.loads(captured.out) == expected_output
    mock_database_handler.get_chat_history.assert_called_once_with(chat_id)


def test_convert_tuples_to_dicts():
    tuples = [("user", "Hello"), ("assistant", "Hi!")]
    expected_dicts = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi!"},
    ]

    result = ChatHistoryRequest.convert_tuples_to_dicts(tuples)
    assert result == expected_dicts

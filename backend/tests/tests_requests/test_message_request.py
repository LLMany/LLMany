from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.llmany_requests.message_request import MessageRequest
from unittest.mock import MagicMock, patch
import json


def test_message_request_initialization():
    mock_model_handler = MagicMock(ModelHandlerFactory)
    mock_database_handler = MagicMock(DatabaseHandler)

    model_type = "gpt-4"
    model = "openai"
    chat_id = 12345
    chat_history = [
        {"role": "user", "content": "Hello there"},
        {"role": "assistant", "content": "General Kenobi"},
    ]
    contents = "Hello!"

    request = MessageRequest(
        mock_model_handler,
        mock_database_handler,
        model_type,
        model,
        chat_id,
        chat_history,
        contents,
    )

    assert request.model_handler_factory == mock_model_handler
    assert request.database_handler == mock_database_handler
    assert request.model_type == model_type
    assert request.model == model
    assert request.chat_ID == chat_id
    assert request.chat_history == chat_history
    assert request.contents == contents


def test_message_request_from_dict():
    mock_database_handler = MagicMock(DatabaseHandler)
    mock_model_handler_factory = MagicMock(ModelHandlerFactory)

    request_data = {"chat_id": 12345, "contents": "Hello!"}

    mock_database_handler.get_model_for_chat.return_value = {
        "model_type": "gpt-4",
        "model": "openai",
    }

    mock_database_handler.get_chat_history.return_value = [
        {"role": "user", "content": "Hello there"},
        {"role": "assistant", "content": "General Kenobi"},
    ]

    request = MessageRequest.from_dict(
        request_data, mock_database_handler, mock_model_handler_factory
    )

    assert request.model_type == "gpt-4"
    assert request.model == "openai"
    assert request.chat_ID == 12345
    assert request.chat_history == [
        {"role": "user", "content": "Hello there"},
        {"role": "assistant", "content": "General Kenobi"},
    ]
    assert request.contents == "Hello!"

    mock_database_handler.get_model_for_chat.assert_called_once_with(12345)
    mock_database_handler.get_chat_history.assert_called_once_with(12345)


def test_message_request_execute():
    mock_database_handler = MagicMock(DatabaseHandler)
    mock_model_handler_factory = MagicMock(ModelHandlerFactory)
    mock_model_handler = MagicMock()

    mock_model_handler_factory.create_model_handler.return_value = mock_model_handler
    mock_model_handler.send_message.return_value = "Hello, user!"

    chat_id = 12345
    chat_history = [
        {"role": "user", "content": "Hello there"},
        {"role": "assistant", "content": "General Kenobi"},
    ]
    contents = "How are you?"

    request = MessageRequest(
        mock_model_handler_factory,
        mock_database_handler,
        "gpt-4",
        "openai",
        chat_id,
        chat_history,
        contents,
    )

    with patch("builtins.print") as mock_print:
        request.execute()

        mock_database_handler.add_message_to_chat.assert_any_call(
            chat_id, "user", "How are you?"
        )
        mock_database_handler.add_message_to_chat.assert_any_call(
            chat_id, "assistant", "Hello, user!"
        )

        mock_model_handler.send_message.assert_called_once_with(
            model="openai", message=contents, history=chat_history
        )

        mock_print.assert_called_once_with(
            json.dumps(
                {"type": "message", "chat_id": 12345, "content": "Hello, user!"}
            ),
            flush=True,
        )

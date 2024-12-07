from unittest.mock import MagicMock
from llmany_backend.database_handler import DatabaseHandler
from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.requests.message_request import MessageRequest


def test_message_request_initialization():
    mock_model_handler = MagicMock(ModelHandlerFactory)
    mock_database_handler = MagicMock(DatabaseHandler)

    model_type = "GPT-4"
    model = "gpt-4-model"
    chat_id = "12345"
    chat_history = "Previous conversation"

    request = MessageRequest(
        mock_model_handler,
        mock_database_handler,
        model_type,
        model,
        chat_id,
        chat_history,
    )

    assert request.model_handler == mock_model_handler
    assert request.database_handler == mock_database_handler
    assert request.model_type == model_type
    assert request.model == model
    assert request.chat_ID == chat_id
    assert request.chat_history == chat_history


def test_execute_message_request(mocker):
    mock_model_handler = MagicMock(ModelHandlerFactory)
    mock_database_handler = MagicMock(DatabaseHandler)

    mock_model_handler.send_message.return_value = "Message sent successfully"

    model_type = "GPT-4"
    model = "gpt-4-model"
    chat_id = "12345"
    chat_history = "Previous conversation"

    request = MessageRequest(
        mock_model_handler,
        mock_database_handler,
        model_type,
        model,
        chat_id,
        chat_history,
    )

    result = request.execute()

    assert result == "Message sent successfully"

    mock_model_handler.send_message.assert_called_once_with(
        model_type=model_type, model=model, chat_id=chat_id, chat_history=chat_history
    )

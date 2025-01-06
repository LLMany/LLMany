from unittest.mock import MagicMock

from llmany_backend.model_handlers.openai_handler import OpenAIHandler


def test_send_message(mocker):
    mock_openai_instance = MagicMock()
    mock_choice = MagicMock()
    mock_choice.message.content = "Hello, this is Skynet!"
    mock_openai_instance.chat.completions.create.return_value = MagicMock(
        choices=[mock_choice]
    )
    mocker.patch(
        "llmany_backend.model_handlers.openai_handler.OpenAI",
        return_value=mock_openai_instance,
    )

    handler = OpenAIHandler(api_key=" ")

    response = handler.send_message(model="gpt-4", message="Hello", history=[])

    assert response == "Hello, this is Skynet!"

    mock_openai_instance.chat.completions.create.assert_called_once_with(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello"}],
    )

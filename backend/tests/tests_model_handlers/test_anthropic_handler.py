from unittest.mock import MagicMock, create_autospec
from anthropic.types import TextBlock

from llmany_backend.model_handlers import AnthropicHandler


def test_send_message(mocker):
    mock_openai_instance = MagicMock()
    mock_choice = create_autospec(TextBlock)
    mock_choice.text = "Hello, this is Skynet!"
    mock_openai_instance.messages.create.return_value = MagicMock(content=[mock_choice])
    mocker.patch(
        "llmany_backend.model_handlers.anthropic_handler.Anthropic",
        return_value=mock_openai_instance,
    )

    handler = AnthropicHandler(api_key=" ")

    response = handler.send_message(model="3.5-sonnet", message="Hello", history=[])

    assert response == "Hello, this is Skynet!"

    mock_openai_instance.messages.create.assert_called_once_with(
        max_tokens=1024,
        model="3.5-sonnet",
        messages=[{"role": "user", "content": "Hello"}],
    )

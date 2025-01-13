from unittest.mock import MagicMock
from llmany_backend.model_handlers.grok_handler import GrokHandler


def test_send_message(mocker):
    mock_openai_instance = MagicMock()
    mock_choice = MagicMock()
    mock_choice.message.content = "Hello, this is Grok!"
    mock_openai_instance.chat.completions.create.return_value = MagicMock(
        choices=[mock_choice]
    )

    mocker.patch(
        "llmany_backend.model_handlers.grok_handler.OpenAI",
        return_value=mock_openai_instance,
    )

    handler = GrokHandler(api_key="dummy_api_key")

    response = handler.send_message(model="grok-beta", message="Hello", history=[])

    assert response == "Hello, this is Grok!"
    mock_openai_instance.chat.completions.create.assert_called_once_with(
        model="grok-beta",
        messages=[{"role": "user", "content": "Hello"}],
    )

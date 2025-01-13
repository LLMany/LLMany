from unittest.mock import MagicMock

from llmany_backend.model_handlers import QwenHandler


def test_send_message(mocker):
    mock_openai_instance = MagicMock()
    mock_choice = MagicMock()
    mock_choice.message.content = "Hello, this is Skynet!"
    mock_openai_instance.chat.completions.create.return_value = MagicMock(
        choices=[mock_choice]
    )
    mocker.patch(
        "llmany_backend.model_handlers.qwen_handler.OpenAI",
        return_value=mock_openai_instance,
    )

    handler = QwenHandler(api_key=" ")

    response = handler.send_message(model="qwen-plus", message="Hello", history=[])

    assert response == "Hello, this is Skynet!"

    mock_openai_instance.chat.completions.create.assert_called_once_with(
        model="qwen-plus",
        messages=[{"role": "user", "content": "Hello"}],
    )

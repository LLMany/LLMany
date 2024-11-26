from llmany_backend.model_handlers.anthropic_handler import AnthropicHandler

def test_send_message(mocker):
    mock_create = mocker.patch("AnthropicHandler.client.messages.create")
    mock_create.return_value = {
        "content": "Hello, this is Skynet!"
    }

    handler = AnthropicHandler()

    response = handler.send_message("Hello")

    assert response == "Hello, this is Skynet!"

    mock_create.assert_called_once_with(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello"}],
    )
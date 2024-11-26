from llmany_backend.model_handlers.openai_handler import OpenAIHandler

def test_send_message(mocker):
    mock_create = mocker.patch("client.chat.completions.create")
    mock_create.return_value = {
        "choices": [{"message": {"content": "Hello, this is Skynet!"}}]
    }

    handler = OpenAIHandler()

    response = handler.send_message("Hello")

    assert response == "Hello, this is Skynet!"

    mock_create.assert_called_once_with(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello"}],
    )
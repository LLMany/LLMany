from llmany_backend.model_handlers.google_handler import GoogleHandler

def test_send_message(mocker):
    mock_create = mocker.patch("GoogleHandler.model.generate_content")
    mock_create.return_value = {"text": "Hello, this is Skynet!"}
    

    handler = GoogleHandler()

    response = handler.send_message("Hello")

    assert response == "Hello, this is Skynet!"

    mock_create.assert_called_once_with(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello"}],
    )
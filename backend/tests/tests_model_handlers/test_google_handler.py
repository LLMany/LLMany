from llmany_backend.model_handlers.google_handler import GoogleHandler


def test_send_message(mocker):
    mock_generative_model = mocker.patch(
        "llmany_backend.model_handlers.google_handler.genai.GenerativeModel"
    )
    mock_chat = mocker.Mock()
    mock_generative_model.return_value.start_chat.return_value = mock_chat

    mock_chat.send_message.return_value.text = "Hello, this is Skynet!"

    handler = GoogleHandler("fake_api_key")

    response = handler.send_message(model="gemini-1.5", message="Hello", history=[])

    assert response == "Hello, this is Skynet!"
    mock_generative_model.assert_called_once_with(model_name="gemini-1.5")
    mock_generative_model.return_value.start_chat.assert_called_once_with(history=[])
    mock_chat.send_message.assert_called_once_with("Hello")

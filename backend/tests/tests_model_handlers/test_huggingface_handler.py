from unittest.mock import MagicMock

from llmany_backend.model_handlers import HuggingfaceHandler


def test_send_message(mocker):
    mock_pipeline = MagicMock()
    mock_pipeline.return_value = [
        {"generated_text": [{"content": "Hello, this is Skynet!"}]}
    ]

    mocker.patch(
        "llmany_backend.model_handlers.huggingface_handler.pipeline",  # Replace with your actual path
        return_value=mock_pipeline,
    )

    handler = HuggingfaceHandler()

    response = handler.send_message(
        model="Qwen/Qwen2.5-Coder-1.5B-Instruct", message="Hello", history=[]
    )

    assert response == "Hello, this is Skynet!"

    mock_pipeline.assert_called_once_with(
        [{"role": "user", "content": "Hello"}], max_new_tokens=512
    )

import pytest
from sqlite3 import connect

from llmany_backend.request_handler import RequestHandler
from llmany_backend.database_handler_factory import DatabaseHandlerFactory
from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.requests import (
    AllChatsRequest,
    DeleteChatRequest,
    ChatHistoryRequest,
    MessageRequest,
    NewChatRequest,
)


@pytest.mark.parametrize(
    "request_string, expected_dict",
    [
        (
            "{" '"type": "new_chat",' '"model_type": "OpenAI",' '"model": "GPT-4o"}',
            {"type": "new_chat", "model_type": "OpenAI", "model": "GPT-4o"},
        ),
        (
            '{"type": "delete_chat", "chat_id": 1234}',
            {
                "type": "delete_chat",
                "chat_id": 1234,
            },
        ),
        (
            '{"type": "all_chats"}',
            {
                "type": "all_chats",
            },
        ),
        (
            '{"type": "chat_history", "chat_id": "1234"}',
            {"type": "chat_history", "chat_id": "1234"},
        ),
        (
            '{"type": "message", "chat_id": "1234", "contents": "Hello world!"}',
            {"type": "message", "chat_id": "1234", "contents": "Hello world!"},
        ),
    ],
)
def test_parse(request_string, expected_dict, temp_file, monkeypatch):
    handler = RequestHandler(
        database_handler_factory=DatabaseHandlerFactory(),
        model_handler_factory=ModelHandlerFactory(),
        connection=connect(temp_file),
    )

    request_data = handler.parse(request_json=request_string)
    assert request_data == expected_dict


@pytest.mark.parametrize(
    "request_data, expected_request_class",
    [
        ({"type": "all_chats"}, AllChatsRequest),
        ({"type": "delete_chat", "chat_id": "c1"}, DeleteChatRequest),
        ({"type": "chat_history", "chat_id": "c1"}, ChatHistoryRequest),
        (
            {"type": "new_chat", "model_type": "OpenAI", "model": "Gpt-4o"},
            NewChatRequest,
        ),
        ({"type": "message", "chat_id": "c1"}, MessageRequest),
    ],
)
def test_create_request(request_data, expected_request_class, temp_file):
    handler = RequestHandler(
        database_handler_factory=DatabaseHandlerFactory(),
        model_handler_factory=ModelHandlerFactory(),
        connection=connect(temp_file),
    )
    request = handler.create_request(request_data)

    assert isinstance(request, expected_request_class)

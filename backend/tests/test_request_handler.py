import pytest

from llmany_backend.request_handler import RequestHandler
from llmany_backend.database_handler_factory import DatabaseHandlerFactory
from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.requests import AllChatRequest, DeleteChatRequest, ChatHistoryRequest, MessageRequest, NewChatRequest


@pytest.mark.parametrize("request, expected_dict", (""))
def test_parse(request, expected_dict, monkeypatch):
    monkeypatch.setattr('bultins.input', lambda _ : request)
    handler = RequestHandler(database_handler_factory=DatabaseHandlerFactory(), 
                             model_handler_factory=ModelHandlerFactory())
    
    request_data = handler.parse()
    assert request_data == expected_dict
    

@pytest.mark.parametrize("request_data, expected_request_class", [
    ({"type": "all_chat"}, AllChatRequest),
    ({"type": "delete_chat", "chat_id": "c1"}, DeleteChatRequest),
    ({"type": "chat_history", "chat_id": "c1"}, ChatHistoryRequest),
    ({"type": "new_chat", "model_type": "OpenAI", "model": "Gpt-4o"}, NewChatRequest),
    ({"type": "message", "chat_id": "c1"}, MessageRequest), 
])
def test_create_request(request_data, expected_request_class):
    handler = RequestHandler(database_handler_factory=DatabaseHandlerFactory(), 
                             model_handler_factory=ModelHandlerFactory())
    request = handler.create_request(request_data)

    assert isinstance(request, expected_request_class)
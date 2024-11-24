import pytest

from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.model_handlers.anthropic_handler import AnthropicHandler
from llmany_backend.model_handlers.google_handler import GoogleHandler
from llmany_backend.model_handlers.openai_handler import OpenAIHandler


@pytest.mark.parametrize(
        "model_type, model_handler_class",
        [("OpenAI", OpenAIHandler),
         ("Google", GoogleHandler),
         ("Anthropic", AnthropicHandler)]
)
def test_proper_handler_created(model_type, model_handler_class):
    factory = ModelHandlerFactory()
    handler = factory.create_model_handler(model_type)
    assert isinstance(handler, model_handler_class)
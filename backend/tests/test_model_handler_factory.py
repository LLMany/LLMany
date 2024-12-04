import pytest

from llmany_backend.model_handler_factory import ModelHandlerFactory
from llmany_backend.model_handlers import AnthropicHandler, GoogleHandler, OpenAIHandler


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
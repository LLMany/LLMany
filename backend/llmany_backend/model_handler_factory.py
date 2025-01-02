from llmany_backend.model_handler import ModelHandler
from llmany_backend.model_handlers import GoogleHandler, OpenAIHandler, AnthropicHandler 

class ModelHandlerFactory:
    def create_model_handler(self, model_type: str, api_key: str) -> ModelHandler:
        match model_type:
            case "google":
                return GoogleHandler(api_key)
            case "openai":
                return OpenAIHandler(api_key)
            case "anthropic":
                return AnthropicHandler(api_key)
            case _:
                raise ValueError(f"Unsupported model type: {model_type}")
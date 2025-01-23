from llmany_backend.model_handler import ModelHandler
from llmany_backend.model_handlers import (
    GoogleHandler,
    OpenAIHandler,
    AnthropicHandler,
    QwenHandler,
    GrokHandler,
    DeepseekHandler,
    HuggingfaceHandler,
)


class ModelHandlerFactory:
    def create_model_handler(self, model_type: str, api_key: str) -> ModelHandler:
        match model_type:
            case "OpenAI":
                return OpenAIHandler(api_key)
            case "Google":
                return GoogleHandler(api_key)
            case "Anthropic":
                return AnthropicHandler(api_key)
            case "Qwen":
                return QwenHandler(api_key)
            case "Grok":
                return GrokHandler(api_key)
            case "Deepseek":
                return DeepseekHandler(api_key)
            case "HuggingFace":
                return HuggingfaceHandler(api_key)
            case _:
                raise ValueError(f"Unsupported model type: {model_type}")

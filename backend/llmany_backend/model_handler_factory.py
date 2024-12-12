from llmany_backend.model_handler import ModelHandler


class ModelHandlerFactory:
    def create_model_handler(self, model_type: str) -> ModelHandler:
        raise NotImplementedError

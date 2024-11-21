from LLMany.backend.llmany_backend.ModelHandler import ModelHandler


class ModelHandlerFactory:
    def create_model_handler(self, model_type: str) -> ModelHandler:
        return ...
from llmany_backend.model_handler import ModelHandler


class AnthropicHandler(ModelHandler):
    def send_message(self, message: str) -> None:
        pass

    def parse_message(self) -> str:
        return ...

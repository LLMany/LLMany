from llmany_backend.model_handler import ModelHandler


class OpenAIHandler(ModelHandler):
    def send_message(self, message: str) -> None:
        pass

    def parse_message(self) -> str:
        return ...
from llmany_backend.model_handler import ModelHandler


class GoogleHandler(ModelHandler):
    def send_message(self, model: str, messages: list[dict[str, str]]) -> str:
        raise NotImplementedError

    def parse_message(self) -> str:
        raise NotImplementedError

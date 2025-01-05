from llmany_backend.model_handler import ModelHandler


class GoogleHandler(ModelHandler):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def send_message(self, model: str, messages: list[dict[str, str]]) -> str:
        raise NotImplementedError

    def parse_message(self) -> str:
        raise NotImplementedError

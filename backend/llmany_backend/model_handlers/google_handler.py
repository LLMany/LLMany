import google.generativeai as genai

from llmany_backend.model_handler import ModelHandler


class GoogleHandler(ModelHandler):
    def __init__(self, api_key: str):
        self.api_key = api_key
        genai.configure(api_key=api_key)

    def send_message(
        self, model: str, message: str, history: list[dict[str, str]]
    ) -> str:
        assistant = genai.GenerativeModel(model_name=model)
        chat = assistant.start_chat(history=history)
        return chat.send_message(message).text

    def parse_message(self) -> str:
        raise NotImplementedError

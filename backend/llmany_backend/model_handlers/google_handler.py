import google.generativeai as genai

from llmany_backend.model_handler import ModelHandler


class GoogleHandler(ModelHandler):
    def __init__(self, api_key: str):
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.assistant = None

    def send_message(
        self, model: str, message: str, history: list[dict[str, str]]
    ) -> str:
        if self.assistant is None:
            assistant = genai.GenerativeModel(model_name=model)

        chat = assistant.start_chat(history=history)

        content = chat.send_message(message)
        return content.text

    def parse_message(self) -> str:
        raise NotImplementedError

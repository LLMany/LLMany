from openai import OpenAI

from llmany_backend.model_handler import ModelHandler

class OpenAIHandler(ModelHandler):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key) 

    def send_message(self, model: str, messages: list[dict[str:str]]) -> None:
        completion = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return completion.choices[0].message.content

    def parse_message(self) -> str:
        return ...

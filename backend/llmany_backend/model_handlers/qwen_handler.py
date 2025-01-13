from openai import OpenAI

from llmany_backend.model_handler import ModelHandler


class QwenHandler(ModelHandler):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = OpenAI(
            base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
            api_key=api_key,
        )

    def send_message(
        self, model: str, message: str, history: list[dict[str, str]]
    ) -> str:
        history.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(  # type: ignore
            model=model,  # type: ignore
            messages=history,  # type: ignore
        )
        return (
            completion.choices[0].message.content
            if completion.choices[0].message.content is not None
            else "An unexpected error occurred, please try sending the message again"
        )

    def parse_message(self) -> str:
        raise NotImplementedError

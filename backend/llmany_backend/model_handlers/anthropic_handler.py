from anthropic import Anthropic

from llmany_backend.model_handler import ModelHandler


class AnthropicHandler(ModelHandler):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = Anthropic(api_key=api_key)

    def send_message(
        self, model: str, message: str, history: list[dict[str, str]]
    ) -> str:
        history.append({"role": "user", "content": message})
        completion = self.client.messages.create(  # type: ignore
            max_tokens=1024,
            model=model,  # type: ignore
            messages=history,  # type: ignore
        )
        return (
            completion.content[0].model_dump()["text"]
            if completion.content is not None
            else "An unexpected error occurred, please try sending the message again"
        )

    def parse_message(self) -> str:
        raise NotImplementedError

from transformers import pipeline

from llmany_backend.model_handler import ModelHandler


class HuggingfaceHandler(ModelHandler):
    def __init__(self):
        pass

    def send_message(
        self, model: str, message: str, history: list[dict[str, str]]
    ) -> str:
        history.append({"role": "user", "content": message})

        assistant = pipeline("text-generation", model=model, device_map="auto")

        output = assistant(history, max_new_tokens=512)
        return output[0]["generated_text"][-1]["content"]

    def parse_message(self) -> str:
        raise NotImplementedError

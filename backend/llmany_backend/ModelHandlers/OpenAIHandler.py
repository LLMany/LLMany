from LLMany.backend.llmany_backend.ModelHandler import ModelHandler


class OpenAIHandler(ModelHandler):
    def send_message(self, message: str) -> None:
        pass

    def parse_message(self) -> str:
        return ...
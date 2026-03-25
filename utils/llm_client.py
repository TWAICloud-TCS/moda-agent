from autogen_ext.models.openai import OpenAIChatCompletionClient


class LLMClient(OpenAIChatCompletionClient):
    def __init__(self, model: str, api_key: str, base_url: str, **kwargs) -> None:
        super().__init__(
            model=model,
            api_key=api_key,
            base_url=base_url,
            model_info={
                "vision": True,
                "function_calling": True,
                "json_output": True,
                "family": "unknown",
                "structured_output": True,
                "multiple_system_messages": True,
            },
            **kwargs
        )
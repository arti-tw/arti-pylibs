import os

from langchain_anthropic.chat_models import ChatAnthropic

from .base import BaseModel, ManualJsonFormatModel


class ClaudeModel(BaseModel):
    def get_core_model(self, name: str = ""):
        name = name or os.getenv("ANTHROPIC_CLAUDE_MODEL")
        return ChatAnthropic(model=name)

    def generate_image_data(self, base64_image: str) -> dict:
        return {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": base64_image,
            },
        }


class ClaudeJsonModel(ClaudeModel, ManualJsonFormatModel):
    pass

import os

from langchain_openai import ChatOpenAI

from .base import BaseModel


class GptModel(BaseModel):
    def get_core_model(self, name: str = ""):
        name = name or os.getenv("OPENAI_GPT_MODEL")
        return ChatOpenAI(model=name)

    def generate_image_data(self, base64_image: str) -> dict:
        return {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}",
            },
        }


class GptJsonModel(GptModel):
    def get_core_model(self, name: str = ""):
        model = super().get_core_model(name)
        model.bind(response_format={"type": "json_object"})
        return model

import os

from langchain_google_genai import ChatGoogleGenerativeAI

from .base import BaseModel, ManualJsonFormatModel


class GeminiModel(BaseModel):
    def get_core_model(self, name: str = ""):
        name = name or os.getenv("GOOGLE_GEMINI_MODEL")
        return ChatGoogleGenerativeAI(model=name)

    def generate_image_data(self, base64_image: str) -> dict:
        return {
            "type": "image_url",
            "image_url": f"data:image/png;base64,{base64_image}",
        }


class GeminiJsonModel(GeminiModel, ManualJsonFormatModel):
    pass

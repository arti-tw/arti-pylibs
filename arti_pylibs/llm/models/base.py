from abc import ABC, abstractmethod

from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class BaseModel(ABC):
    def __init__(
        self,
        system_prompt: ChatPromptTemplate | str,
        model_name: str = "",
        callbacks: list[BaseCallbackHandler] = None,
    ):
        if isinstance(system_prompt, str):
            system_prompt = self.generate_system_prompt_template(system_prompt)

        self.model = self.get_core_model(model_name)
        self.chain = system_prompt | self.model
        if callbacks:
            self.chain = self.chain.with_config(callbacks=callbacks)
        self.message_history: list[BaseMessage] = []

    def send_message(self, message: HumanMessage):
        self.message_history.append(message)
        self.pre_invoke()
        ai_response = self.chain.invoke({"messages": self.message_history})
        self.message_history.append(ai_response)
        self.post_invoke()
        return self.message_history[-1]

    def pre_invoke(self):
        pass

    def post_invoke(self):
        pass

    @abstractmethod
    def get_core_model(self, name: str = "") -> BaseChatModel:
        pass

    @abstractmethod
    def generate_image_data(self, base64_image: str) -> dict:
        pass

    def generate_system_prompt_template(self, prompt: str):
        return ChatPromptTemplate.from_messages(
            [
                ("system", prompt),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )


class ManualJsonFormatModel(BaseModel):
    def pre_invoke(self):
        self.message_history.append(AIMessage(content="{"))

    def post_invoke(self):
        ai_response = self.message_history.pop()
        _ = self.message_history.pop()
        ai_response.content = "{" + ai_response.content
        self.message_history.append(ai_response)

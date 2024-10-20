from arti_pylibs.llm.callbacks import LangfuseCallbackHandler


class BaseLLMApp:
    def __init__(self, callback_args: dict = None):
        if callback_args:
            callback = LangfuseCallbackHandler(**callback_args)
        self.callbacks = [callback] if callback else []

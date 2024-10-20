import os

from langfuse.callback import CallbackHandler


class LangfuseCallbackHandler(CallbackHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(
            host=os.getenv("LANGFUSE_HOST"),
            public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
            secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
            *args,
            **kwargs,
        )

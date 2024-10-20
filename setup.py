from setuptools import setup, find_packages

setup(
    name="arti-pylibs",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain-anthropic",
        "langchain-google-genai",
        "langchain-openai",
        "langfuse",
        'pillow',
    ],
    author="Arti TW",
    description="A shared library of utilities and functions used across Arti repositories",
    python_requires=">=3.9",
)

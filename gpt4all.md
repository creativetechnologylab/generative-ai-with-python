# GPT4All

## Introduction

GPT4All is capable of running LLMs locally, even on computers without GPUs.

## Installation

The GPT4All library can be installed with pip. First, let's create a Conda environment for using the library. We can do this with the command `conda create --name gpt4all python=3.10`. When the environment has been completed then it can be activated with the command `conda activate gpt4all`.

Now we can install the GPT4All library to this environment with the command `pip install gpt4all`.

![](images/gpt4all/pip-install-gpt4all.gif)

Now create a folder for some code to test out the library and open it in the terminal or navigate to it with the Miniforge prompt. Create a Python file, and name it `hello-test.py`. Open this file in your text editor/IDE of choice and then enter the following code:

```python
from gpt4all import GPT4All

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# generate a reply and print it
print(model.generate("Hello!"))
```

Here we are telling GPT4All to download the Orca Mini model, and then simply saying Hello. But this can generate some weird output. Here are some examples of what I got:

![](images/gpt4all/hello.gif)

This code is not ideal for when we want to have a conversation with the model, and keep things in its history. But we can try and see how it behaves when we ask it for factual infomration. Try adding the line of code to the file:

```python
print(model.generate("What is the capital of France?"))
```

Now we can try running this again, and see if its answers make more sense. It doesn't really "know" what to say to something like a "hello" in the same way a person does, but this time we are asking it to state a fact. You may get a response like this:

![](images/gpt4all/france.gif)

Despite running the code more than once, the response still hasn't been very useful. 
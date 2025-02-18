# GPT4All

## Introduction

GPT4All is capable of running LLMs locally, even on computers without GPUs.

## Installation

The GPT4All library can be installed with pip. First, let's create a Conda environment for using the library. We can do this with the command `conda create --name gpt4all python=3.10`. When the environment has been completed then it can be activated with the command `conda activate gpt4all`.

Now we can install the GPT4All library to this environment with the command `pip install gpt4all`.

![](images/gpt4all/pip-install-gpt4all.gif)

## Generating Responses

### Without a Session

In GPT4All we can interact with models with or without a _session_. A session is capable of storing conversation history, so if we simply ask it to generate replies, it will have no memory of anything we asked it before.

Now create a folder for some code to test out the GPT4All and open it in the terminal or navigate to it with the Miniforge prompt. Create a Python file, and name it `hello-test.py`. Open this file in your text editor/IDE of choice and then enter the following code:

```python
from gpt4all import GPT4All

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# generate a reply and print it
print(model.generate("Hello!"))
```

Here we are telling GPT4All to download the Orca Mini model, and then simply saying Hello. But this can generate some weird output. Here are some examples of what I got:

![](images/gpt4all/hello.gif)

Let's see how it behaves when we ask it for factual infomration. Try adding the line of code to the file:

```python
print(model.generate("What is the capital of France?"))
```

Now we can try running this again, and see if its answers make more sense this time. It doesn't really _know_ what to say to something like a "hello" in the same way a person does, but this time we are asking it to state a fact. You may get a response like this:

![](images/gpt4all/france.gif)

Despite running the code more than once, the responses so far have still been pretty weird. In the documentation, it is advised to use a _session_ instead when running a model.

### With a Session

Now create another file named `session-test.py` in the same directory, and try the following code:

```python
from gpt4all import GPT4All

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# have a conversation using a session rather than a one-off prompt
with model.chat_session():
    print(model.generate("Hello!"))
    print(model.generate("Pick one: cats or dogs?"))
```

When you run it now, you may get something that sounds a lot more sensible:

![](images/gpt4all/session-cats-dogs.gif)

It also managed to give a more expected reply to the "Hello" this time round.

### System Prompts

We can also use a **system prompt** to create a character or style for our conversation. These are the very first prompt that the model receives.



## Managing Hallucination
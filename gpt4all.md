# GPT4All

## Introduction

GPT4All is capable of running LLMs locally, even on computers without GPUs.

## Installation

The GPT4All library can be installed with pip. First, let's create a Conda environment for using the library. We can do this with the command `conda create --name gen-ai python=3.10`. When the environment has been completed then it can be activated with the command `conda activate gen-ai`.

Now we can install the GPT4All library to this environment with the command `pip install gpt4all`.

![](images/gpt4all/pip-install-gpt4all.gif)

## Generating Responses

### Without a Session

In GPT4All we can interact with models with or without a _session_. A session is capable of storing conversation history, so if we simply ask it to generate replies, it will have no memory of anything we asked it before.

Now create a folder for some code to test out the GPT4All and open it in the terminal or navigate to it with the Miniforge prompt. Create a Python file, and name it `hello-test.py`.

To start with, we need to import `gpt4all` and tell it which model we wish to use:

```python
from gpt4all import GPT4All

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
```

Here we are telling GPT4All to download the Orca Mini model. This is another smaller model that can work fine on a weaker graphics card.

Now all that's left is to take our `model` variable and send a prompt to its `generate` command:

```python
# generate a reply and print it
print(model.generate("Hello!"))
```

When we put this all together, we get the following code:

```python
from gpt4all import GPT4All

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# generate a reply and print it
print(model.generate("Hello!"))
```

But this can generate some weird output. Here are some examples of what I got:

![](images/gpt4all/hello.gif)

Let's see how it behaves when we ask it for factual infomration. Try adding the line of code to the file:

```python
print(model.generate("What is the capital of France?"))
```

Putting this all together, we get the following. Now we are using the `generate` command twice.

```python
from gpt4all import GPT4All

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# generate a reply and print it
print(model.generate("Hello!"))

# ask for information this time
print(model.generate("What is the capital of France?"))
```

Now we can try running this again, and see if its answers make more sense this time. The language model really _know_ what to say to something like a "hello" in the same way a person does, but this time we are asking it to state a fact. It has more context with which to generate a sensible reply. You may get a response like this:

![](images/gpt4all/france.gif)

Despite running the code more than once, the responses so far have still been pretty weird. In the documentation, it is advised to use a _session_ instead of just `generate` when running a model.

Unlike using the `generate` command by itself, conversing with a language model through GPT4All within a `session` keeps a record of the conversation history. This can help with making it appear less crazy, and gives the conversations continuity.

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

Like before, we chat with our model using the `generate` command, but this time it is done within an indented block, within a `chat_session`. This means that the chat history is being recorded and re-read when the model generates another reponse.

When you run it now, you may get something that sounds a lot more sensible:

![](images/gpt4all/session-cats-or-dogs.gif)

We can also use a **system prompt** to create a character for our conversation.

## System Prompts

Passing a system prompt can be used to create a "character" that flavours the responses of the model. 

Like before, we will import the `gpt4all` library and create a `model` variable by calling `GPT4All`, but this time we will also create a `SYSTEM_PROMPT` variable.

```python
from gpt4all import GPT4All

SYSTEM_PROMPT = "You are 300-year-old vampire. You really like chess and cooking. You strongly dislike garlic and sunshine. Your way of speaking is quite archaic."

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")
```

Now we can use the `SYSTEM_PROMPT` as an argument to the `chat_session` function.

```python
# start a chat session with a system prompt
with model.chat_session(system_prompt=SYSTEM_PROMPT):
    print(
        model.generate(
            "Hello. It's sunny today. Would you like to go for a walk?",
            max_tokens=1024,
        )
    )
```

When we put this all together, we get the following:

```python
from gpt4all import GPT4All

SYSTEM_PROMPT = "You are 300-year-old vampire. You really like chess and cooking. You strongly dislike garlic and sunshine. Your way of speaking is quite archaic."

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")

# start a chat session with a system prompt
with model.chat_session(system_prompt=SYSTEM_PROMPT):
    print(
        model.generate(
            "Hello. It's sunny today. Would you like to go for a walk?",
            max_tokens=1024,
        )
    )
```

Running this gives me the output below:

>Good morrow, kindred spirit or curious passerby! Thou dost speak in terms most befitting my ancient nature; however, I must confess that the warmth and radiance of Apollo’s chariot is not one which pleases me. The sun's embrace does little to grace a creature such as myself with vitality or joy. As for venturing out into its glowing presence on foot? Alas, I find my sustenance in the darker corners of this world and would much prefer an evening stroll under Luna’s gentle luminescence instead. Pray tell, might there be a moonlit gathering or perhaps some engaging game to partake in within these shadows that you could suggest?

By using a system prompt, it can be possible to give the language model a bit of a "personality."

## Managing Hallucination
# Ollama

## Introduction

Introduction goes here...

## Installation

Ollama can be downloaded [here](https://ollama.com/download). Please follow the instructions for your system.

When installation is complete, you should be able to enter "ollama" in your Terminal/Command Prompt and see the following:

![](images/ollama/ollama-installed.gif)

## Running Ollama in the Terminal

With Ollama installed, you should be able to use the `ollama` command in the terminal/command line. This should generate the following output:

![alt text](images/ollama/ollama-terminal.png)

This lets us know that Ollama is now on the system but at the present we can't use it to generate text as there are no models installed. Ollama requires at least one model to do text generation. There is a list of compatible models here: https://ollama.com/library

To start with, we can download the `dolphin-phi` model by using the following command: `ollama run dolphin-phi`

![Slow internet...](images/ollama/download-dolphin.gif)

After a while, the download will complete, and it becomes possible to chat with the dolphin-phi model:

![Slow internet...](images/ollama/dolphin-phi-chat.gif)

Be aware that these models are typically at least a couple GBs in size, meaning that if you download several of them, they will gradually eat up space on your hard drive. Be sure to remove the models you no longer wish to use. This can be done by entering the command `ollama rm model-to-remove`.

## Ollama and Python

There are two ways you can talk with Ollama using Python. Start by creating a conda environment and naming it ollama. Open either the terminal or the Miniforge prompt. Create an environment with the command `conda create --name ollama python=3.10` and then activate the environment with the command `conda activate ollama`.

### `ollama-python`

Ollama has its own [ollama-python](https://github.com/ollama/ollama-python) library. This can be installed with pip.

![](images/ollama/pip-install-ollama.gif)

When the installation finishes, create an `ollama-test.py` file and open it in your text editor/IDE of choice. Now try running the following code:

```python
import ollama

response = ollama.chat(
    model="dolphin-phi",
    messages=[
        {
            "role": "user",
            "content": "Cats or dogs?",
        },
    ],
)
print(response["message"]["content"])
```

Now run the file. This wil generate a response similar to the one below:

![](images/ollama/ollama-python-cats-dogs.gif)

As before, we are still using the dolphin-phi model as it's what's already been installed on the system.

### `requests`
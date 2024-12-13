# text-generation-webui

## Introduction

text-generation-webui is another tool that allows us to work with language. text-generation-webui also makes it possible to _fine-tune_ existing language models. This enables us to feed a model some chunk of text, and have it absorb knowledge from it, or copy the style of the text we provide.

## Installation and Running

Head over to the text-generation-webui [repo](https://github.com/oobabooga/text-generation-webui) and clone or download it. 

Navigate to the text-generation-webui with the terminal/command prompt and run the start script for your system (Mac, Linux, Windows) by entering `start_windows.bat`, `start_mac.sh` or `start_linux.sh`.

On the first run, some requirements will be installed. This should take a few minutes. Once that is complete, you should see a URL in your terminal to the web UI. THis will most likely be http://127.0.0.1:7860. Open this link in your preferred web browser.

## Web UI Interface

The first thing that you should see upon opening the link is the Chat tab. This is where we can talk to language models via the web interface. We are not restricted to only talking to models through this interface, but it can be used to testing out how much a language model has been "flavoured" by fine-tuning with your custom data.

![](images/text-generation-webui/chat-tab.png)

Now try to have a conversation with the assistant? What happens?

![](images/text-generation-webui/pancake-no-model.png)

At the moment, asking questions generated an empty "response." Because this is our first time using text-generation-webui, we don't have any models installed yet. So we have nothing to talk to. To fix this, we can head over to the Model tab and download our first model.

The terminal also lets us know that we currently have no Model loaded:

![](images/text-generation-webui/no-model-terminal.png)

## Downloading a Model

On the top panel, click on the Model tab. 



## Fine-Tuning a Model

## Creating Characters

## API
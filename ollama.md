# Ollama

## Introduction

Introduction goes here...

## Installation

TODO.

## Running Ollama in the Terminal

With Ollama installed, you should be able to use the `ollama` command in the terminal/command line. This should generate the following output:

![alt text](images/ollama/ollama-terminal.png)

This lets us know that Ollama is now on the system but at the present we can't use it to generate text as there are no models installed. Ollama requires at least one model to do text generation. There is a list of compatible models here: https://ollama.com/library

To start with, we can download the `dolphin-phi` model by using the following command: `ollama run dolphin-phi`

![Slow internet...](images/ollama/download-dolphin.gif)

Be aware that these models are typically at least a couple GBs in size, meaning that if you download several of them, they will gradually eat up space on your hard drive.
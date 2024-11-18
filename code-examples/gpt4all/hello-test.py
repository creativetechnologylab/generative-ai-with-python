from gpt4all import GPT4All

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# generate a reply and print it
print(model.generate("Hello!"))

# ask for information this time
print(model.generate("What is the capital of France?"))
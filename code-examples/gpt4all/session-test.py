from gpt4all import GPT4All

# choose a model to chat with - this will download it if it isn't already present on your machine
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# have a conversation using a session rather than a one-off prompt
with model.chat_session():
    print(model.generate("Hello!"))
    print(model.generate("Pick one: cats or dogs?"))

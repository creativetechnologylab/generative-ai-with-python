from gpt4all import GPT4All

# change the path for where the deepseek gguf was downloaded
DEEPSEEK_PATH = "/home/work/llm-models/DeepSeek-R1-Distill-Llama-8B-Q4_0.gguf"
model = GPT4All(DEEPSEEK_PATH)

# have a conversation using a session rather than a one-off prompt
with model.chat_session():
    print(model.generate("Hello!"))
    print(model.generate("Pick one: cats or dogs?"))

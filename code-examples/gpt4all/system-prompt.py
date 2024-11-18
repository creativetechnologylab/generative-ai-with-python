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

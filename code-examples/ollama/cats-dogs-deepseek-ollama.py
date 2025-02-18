import ollama

response = ollama.chat(
    model="deepseek-r1:14b",
    messages=[
        {
            "role": "user",
            "content": "Cats or dogs?",
        },
    ],
)
print(response["message"]["content"])
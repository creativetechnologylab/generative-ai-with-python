import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

data = {
    "model": "deepseek-r1:14b",
    "prompt": "Cats or dogs?",
    "stream": False,
}
response = requests.post(OLLAMA_API_URL, json=data)

if response.status_code == 200:
    result = response.json()
    print(result["response"])
else:
    print(f"Failed to get a response: {response.status_code}")
import requests
import base64

OLLAMA_API_URL = "http://localhost:11434/api/generate"

with open("clown.jpg", "rb") as image_file:
    image = base64.b64encode(image_file.read()).decode("utf-8")

data = {
    "model": "moondream",
    "prompt": "What's in this image?",
    "images": [image],
    "stream": False,
}
response = requests.post(OLLAMA_API_URL, json=data)

if response.status_code == 200:
    result = response.json()
    print(result["response"])
else:
    print(f"Failed to get a response: {response.status_code}")
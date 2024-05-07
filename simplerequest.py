import requests
import json

api = "http://localhost:11434/api/chat"

payload = {
    "model": "phi3",
    "messages": [
        {
            "role": "user",
            "content": "Hi there!",
        }
    ],
    "stream": False
}

print("Asking: Hi There!")
post_response = requests.post(api, json=payload)
post_response_json = post_response.json()
print("Phi3 is responding:")
print(post_response_json['message']['content'])
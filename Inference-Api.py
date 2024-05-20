import os
from dotenv import load_dotenv
import requests
from IPython.display import Audio
import io
from PIL import Image

load_dotenv()

HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_HUB_API')
# Text generation
API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


phi3_mini_4k_user = "<|user|>\n "
phi3_mini_4k_end = "<|end|>\n"
phi3_mini_4k_assistant = "<|assistant|>"

# output = query({
#     "inputs": f"{phi3_mini_4k_user}Can you write a story about an english sir and his beloved woman?{phi3_mini_4k_end}"
#               f"{phi3_mini_4k_assistant}",
#     "options": {
#         "wait_for_model": True
#     }
# })

# generated_text = output[0]['generated_text']
# assistant_text = generated_text.split(phi3_mini_4k_assistant)
# print(assistant_text[1].strip())

# Image generation
IMAGE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"


def image_query(payload):
    response = requests.post(IMAGE_API_URL, headers=headers, json=payload)
    # with open("out.wav", "wb") as f:
    #     f.write(response.content)
    return response.content


image_bytes = image_query({
    "inputs": "Astronaut riding a horse",
    "options":{
        "wait_for_model":True
    }
})
# print("content", image_bytes)
# print("Speeching", audio_bytes)
Image.open(io.BytesIO(image_bytes))


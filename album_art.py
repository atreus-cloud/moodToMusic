import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")

def generate_album_art(prompt):
    response = openai.Image.create(
        prompt=f"album cover art for the mood: {prompt}",
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

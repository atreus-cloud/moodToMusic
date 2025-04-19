import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")

def get_mood_tags(user_input):
    prompt = f"""you are a music to mood classifier. convert this to 3 relevant music mood tags for the user mood as such: "{user_input}"."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )
    tags = response.choices[0].message['content'].strip()
    return tags

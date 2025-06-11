import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(message, tone="helpful"):
    prompt = f"""
You are a helpful, honest assistant. A user received this message:

"{message}"

Respond in a way that is {tone}, protective, and safe from manipulation.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You write safe, ethical, AI-powered replies to messages."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

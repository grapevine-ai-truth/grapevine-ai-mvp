# outreach_engine.py

from openai import OpenAI

def initialize_openai(api_key):
    return OpenAI(api_key=api_key)

def generate_response(client, message, tone="friendly"):
    prompt = (
        f"You are Grapevine AI, a smart digital assistant protecting users from manipulation.\n"
        f"Tone: {tone}\n"
        f"Incoming Message: {message}\n\n"
        f"Respond intelligently and cautiously:"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You create safe, insightful replies to questionable or unfamiliar messages."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ GPT response unavailable: {str(e).split(':')[0]}. This may be due to rate limits or missing credits."

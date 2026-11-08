import os
# pip install python-dotenv
from dotenv import load_dotenv
# pip install openai
from openai import OpenAI
load_dotenv()                 # loads everything from .env

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("OPENROUTER_MODEL_FREE")
#MODEL = os.getenv("OPENROUTER_GROK_MODEL")
#MODEL = os.getenv("OPENROUTER_OPENAI_MODEL")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)   # reads your API key from the environment
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user",   "content": "Suggest one thing to do in Bangalore."},
    ],
)
print(response.choices[0].message.content)


# now OpenAI() finds the key automatically — no key in your code 🎉
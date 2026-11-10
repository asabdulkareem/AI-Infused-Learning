import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("OPENROUTER_MODEL_FREE")
MODEL1 = os.getenv("OPENROUTER_MODEL_FREE")
MODEL2 = os.getenv("OPENROUTER_MODEL_FREE")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_gemini_llm():
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found. Please set it in a .env file.")
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY)
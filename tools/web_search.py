import os
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSearchAPIWrapper

load_dotenv()

GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_web_search_tool():
    if not GOOGLE_CSE_ID or not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_CSE_ID and GOOGLE_API_KEY not found. Please set them in a .env file.")
    return GoogleSearchAPIWrapper(google_api_key=GOOGLE_API_KEY, google_cse_id=GOOGLE_CSE_ID)



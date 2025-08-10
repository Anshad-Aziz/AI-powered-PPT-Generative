import requests
import os
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
PEXELS_URL = "https://api.pexels.com/v1/search"

def get_image_url(query):
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": 1}
    response = requests.get(PEXELS_URL, headers=headers, params=params)
    data = response.json()
    if data.get("photos"):
        return data["photos"][0]["src"]["large"]
    return None

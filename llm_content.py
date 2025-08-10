import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_presentation_content(topic):
    prompt = f"""
    Create a presentation outline about '{topic}'.
    Structure:
    - Title Slide: Title + short intro
    - 3-4 content slides with heading + short paragraph
    - Final slide: Conclusion / Thank you
    Output in JSON format only:
    {{
      "title": "...",
      "intro": "...",
      "slides": [
        {{"heading": "...", "text": "..."}},
        ...
      ],
      "conclusion": "..."
    }}
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Fast free model on Groq
        messages=[
            {"role": "system", "content": "You are a helpful assistant that outputs only clean JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        return None

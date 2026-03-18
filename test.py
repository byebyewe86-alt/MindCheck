
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Her name is Saanvi, ask how is she doing? In a polite and comforting way.   "
        }
    ]
)

print(response.choices[0].message.content)
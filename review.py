import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def review_code(code):

    prompt = f"""
You are an expert Python code reviewer.

Review the following Python code.

Check for:
1. Bugs
2. Security issues
3. Performance improvements
4. Best coding practices

Explain everything in simple language.

Python Code:

{code}
"""
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
    return response.choices[0].message.content

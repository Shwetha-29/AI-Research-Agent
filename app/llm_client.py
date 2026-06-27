import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def ask_llm(prompt):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Research Agent"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 400,
        "temperature": 0.2
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=60
    )

    print("STATUS CODE:", response.status_code)

    if response.status_code != 200:
        print(response.text)

    response.raise_for_status()

    data = response.json()

    if "choices" not in data:
        print("Unexpected response:")
        print(data)
        return None

    return data["choices"][0]["message"]["content"]
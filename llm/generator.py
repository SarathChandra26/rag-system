import requests
from config.settings import OPENROUTER_API_KEY, OPENROUTER_MODEL
from llm.prompts import SYSTEM_PROMPT

def generate_answer(query, context):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Simple RAG System",
        "Content-Type": "application/json"
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {query}"
            }
        ]
    }

    r = requests.post(url, json=payload, headers=headers)
    r.raise_for_status()
    data = r.json()

    return data["choices"][0]["message"]["content"]

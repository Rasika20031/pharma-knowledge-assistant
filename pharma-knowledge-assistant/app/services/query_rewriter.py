import requests


def rewrite_query(
    question: str
):

    prompt = f"""
You are a medical search optimizer.

Rewrite the user's question
into a more specific search query.

Return ONLY the rewritten query.

Question:
{question}
"""

    response = requests.post(

        "http://localhost:11434/api/generate",

        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }

    )

    return (
        response.json()
        .get(
            "response",
            question
        )
        .strip()
    )
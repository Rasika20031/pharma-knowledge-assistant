import requests


def classify_question(question: str):

    prompt = f"""
You are a routing assistant.

Classify the question into one category:

RAG
SQL

Use SQL for:
- sales
- revenue
- numbers
- metrics
- counts
- database information

Use RAG for:
- drug information
- indications
- side effects
- dosage
- document information

Return ONLY:
RAG

or

SQL

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

    response.raise_for_status()

    return response.json()["response"].strip()
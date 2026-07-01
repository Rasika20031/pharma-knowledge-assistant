import requests


def generate_sql_answer(
    question: str,
    sql_query: str,
    sql_result
):

    prompt = f"""
You are a pharmaceutical business assistant.

Use ONLY the SQL Result.

Do not hallucinate.

If SQL Result is empty,
say that no matching records were found.


Question:
{question}

SQL Query:
{sql_query}

SQL Result:
{sql_result}

Provide a concise business-friendly answer.
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

    answer = response.json()["response"]

    return answer.strip()
import requests
import re


def generate_sql(question: str):

    prompt = f"""
You are an SQLite expert.

Database Schema

Table: sales

Columns
- id INTEGER
- product TEXT
- country TEXT
- sales REAL

Rules

- Return ONLY one SQL query.
- Do not explain.
- Do not use markdown.
- Do not use ```sql.
- Do not add comments.
- The first word of your response must be SELECT.
- The query must end with a semicolon.
- Use only the sales table.
- Never invent columns.
- Never invent tables.

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

    raw_response = response.json()["response"]

    print("\n==============================")
    print("RAW SQL RESPONSE")
    print("==============================")
    print(raw_response)

    # Extract SQL statement
    match = re.search(
        r"(SELECT|INSERT|UPDATE|DELETE).*?;",
        raw_response,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        sql_query = match.group(0).strip()
    else:
        sql_query = raw_response.strip()

    print("\n==============================")
    print("EXTRACTED SQL")
    print("==============================")
    print(sql_query)

    return sql_query
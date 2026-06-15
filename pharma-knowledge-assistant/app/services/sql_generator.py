import requests


def generate_sql(question: str):

#     prompt = f"""
# You are a SQL expert.

# Convert the user's question into SQLite SQL.

# Table: sales

# Columns:
# - id
# - product
# - country
# - sales

# Return ONLY the SQL query.

# Question:
# {question}
# """
    prompt = f"""
    You are an SQLite expert.

    Table: sales

    Columns:
    - id
    - product
    - country
    - sales

    Generate ONLY a valid SQLite query.

    Do not explain.
    Do not add markdown.
    Do not add comments.
    Do not add any text before or after the SQL.

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

    sql_query = response.json()["response"]

    return sql_query.strip()
import sqlite3


def execute_sql(sql_query: str):

    conn = sqlite3.connect(
        "app/database/sales.db"
    )

    cursor = conn.cursor()

    try:

        cursor.execute(sql_query)

        rows = cursor.fetchall()

    except Exception as e:

        print(f"SQL Execution Error: {e}")

        rows = []

    finally:

        conn.close()

    return rows
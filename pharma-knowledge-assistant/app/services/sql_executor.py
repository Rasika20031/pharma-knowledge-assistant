import sqlite3


def execute_sql(sql_query: str):

    conn = sqlite3.connect(
        "app/database/sales.db"
    )

    cursor = conn.cursor()

    cursor.execute(sql_query)

    rows = cursor.fetchall()

    conn.close()

    return rows
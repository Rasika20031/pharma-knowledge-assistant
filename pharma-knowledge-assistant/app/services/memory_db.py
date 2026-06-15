import sqlite3


def save_memory(
    session_id,
    question,
    answer
):

    conn = sqlite3.connect(
        "app/database/sales.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chat_memory
        (
            session_id,
            question,
            answer
        )
        VALUES (?, ?, ?)
        """,
        (
            session_id,
            question,
            answer
        )
    )

    conn.commit()
    conn.close()


def get_memory(
    session_id
):

    conn = sqlite3.connect(
        "app/database/sales.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT question, answer
        FROM chat_memory
        WHERE session_id = ?
        ORDER BY id
        """,
        (
            session_id,
        )
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "question": row[0],
            "answer": row[1]
        }
        for row in rows
    ]
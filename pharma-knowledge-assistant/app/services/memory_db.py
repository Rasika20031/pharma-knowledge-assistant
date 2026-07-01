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

    # Check if same question already exists
    cursor.execute(
        """
        SELECT id
        FROM chat_memory
        WHERE session_id = ?
        AND question = ?
        """,
        (
            session_id,
            question
        )
    )

    existing = cursor.fetchone()

    if existing:

        print(
            "Memory already exists. Skipping..."
        )

        conn.close()

        return

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
        LIMIT 5
        """,
        (
            session_id,
        )
    )

    rows = cursor.fetchall()
    rows.reverse()
    conn.close()

    return [
        {
            "question": row[0],
            "answer": row[1]
        }
        for row in rows
    ]
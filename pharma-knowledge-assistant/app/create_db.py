import sqlite3

# conn = sqlite3.connect("database/sales.db")
conn = sqlite3.connect("app/database/sales.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    country TEXT,
    sales INTEGER
)
""")

sales_data = [
    ("Brintellix", "India", 50000),
    ("Brintellix", "USA", 100000),
    ("Brintellix", "Germany", 80000),
    ("Rexulti", "India", 70000),
    ("Rexulti", "USA", 120000),
    ("Abilify", "India", 60000),
    ("Abilify", "USA", 90000)
]
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    question TEXT,
    answer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
cursor.executemany(
    """
    INSERT INTO sales (
        product,
        country,
        sales
    )
    VALUES (?, ?, ?)
    """,
    sales_data
)

conn.commit()

conn.close()

print("Database Created Successfully")
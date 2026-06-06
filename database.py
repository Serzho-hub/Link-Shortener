import sqlite3

DB_NAME = "shortener.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_url(short_code: str, original_url: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO urls (short_code, original_url) VALUES (?, ?)", (short_code, original_url))
    conn.commit()
    conn.close()

def get_original_url(short_code: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT original_url FROM urls WHERE short_code = ?", (short_code,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
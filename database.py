import sqlite3

def init_db():

    conn = sqlite3.connect("soc.db")

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS incidents(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        severity TEXT,

        status TEXT

    )

    """)

    conn.commit()

    conn.close()

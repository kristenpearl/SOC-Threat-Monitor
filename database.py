import sqlite3

DATABASE = "soc.db"

def init_db():

    conn = sqlite3.connect(DATABASE)

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


def add_incident(

    title,

    severity,

    status

):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(

        """

        INSERT INTO incidents

        (

            title,

            severity,

            status

        )

        VALUES

        (?, ?, ?)

        """,

        (

            title,

            severity,

            status

        )

    )

    conn.commit()

    conn.close()


def get_incidents():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM incidents"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

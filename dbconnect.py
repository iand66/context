import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    yield cursor
    conn.commit()
    conn.close()

with db_connection('monty.db') as c:
    c.execute("SELECT * FROM Albums")
    rows = c.fetchall()
    for row in rows:
        print(row)
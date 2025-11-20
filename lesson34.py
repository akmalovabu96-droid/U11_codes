import sqlite3

conn = sqlite3.connect('dastur.db')
curr = conn.cursor()
a = curr.execute("SELECT * FROM main.computer;").fetchall()
print(a)
conn.close()


class DBManager:
    def __init__(self, db_name="dastur.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()


with DBManager() as curr:
    a = curr.execute("SELECT * FROM main.computer;").fetchall()
    print(a)

# with DBManager() as curr:


import sqlite3
from models import User


class AutoCloseCursur(sqlite3.Cursor):
    def __init__(self, connection):
        super().__init__(connection)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def setup():
    with sqlite3.connect("db.sqlite3") as conn:
        with AutoCloseCursur(conn) as cur:
            cur.execute("CREATE TABLE Users (id char, password char)")
        conn.commit()


def add_user(userdata: User):
    with sqlite3.connect("db.sqlite3") as conn:
        with AutoCloseCursur(conn) as cur:
            cur.execute("INSERT INTO Users VALUES (?, ?)", (userdata.id, userdata.password))
        conn.commit()


def check_password(userdata: User):
    with sqlite3.connect("db.sqlite3") as conn:
        with AutoCloseCursur(conn) as cur:
            cur.execute("SELECT password FROM Users WHERE id=?", (userdata.id,))
            return cur.fetchone()[0] == userdata.password


def list_users():
    with sqlite3.connect("db.sqlite3") as conn:
        with AutoCloseCursur(conn) as cur:
            cur.execute("SELECT * FROM Users")
            return cur.fetchall()


def list_user_ids():
    with sqlite3.connect("db.sqlite3") as conn:
        with AutoCloseCursur(conn) as cur:
            cur.execute("SELECT id FROM Users")
            return tuple((data[0] for data in cur.fetchall()))

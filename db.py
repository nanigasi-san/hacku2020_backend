import sqlite3


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
            cur.execute("CREATE TABLE Users (username char, password_hash_md5 char)")
            cur.execute("CREATE TABLE Standings (contest_name char, username char, score int)")
        conn.commit()


def add_user(username: str, password_hash_md5: str):
    with sqlite3.connect("db.sqlite3") as conn:
        with AutoCloseCursur(conn) as cur:
            cur.execute("INSERT INTO Users VALUES (?, ?)", (username, password_hash_md5))
        conn.commit()


def check_password_hash(username: str, password_hash_md5: str):
    with sqlite3.connect("db.sqlite3") as conn:
        with AutoCloseCursur(conn) as cur:
            cur.execute("SELECT password_hash_md5 FROM Users WHERE username=?", (username,))
            return cur.fetchone()[0] == password_hash_md5


def list_users():
    with sqlite3.connect("db.sqlite3") as conn:
        with AutoCloseCursur(conn) as cur:
            cur.execute("SELECT * FROM Users")
            return cur.fetchall()


def list_user_usernames():
    with sqlite3.connect("db.sqlite3") as conn:
        with AutoCloseCursur(conn) as cur:
            cur.execute("SELECT username FROM Users")
            return tuple((data[0] for data in cur.fetchall()))

import sqlite3
import bcrypt


class User:
    def __init__(self, fname: str, lname: str, username: str, password: str):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password

    def login(username: str, password: str):
        con = sqlite3.connect("db/Bookstore.db")  # connect to db
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        row = cur.execute(
            f"SELECT * FROM users WHERE username LIKE \"{username}\";").fetchone()
        print(row)
        print(bcrypt.checkpw(password, row['password_hash']))
        # with open('db/create_tables.sql') as f:
        #     sql_file = f.read()

        # con = sqlite3.connect("db/Bookstore.db")
        # cur = con.cursor()
        # res = cur.executescript(sql_file)
        # con.commit()
        # con.close()

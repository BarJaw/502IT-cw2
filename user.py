from colors import green_text, red_text, blue_text
import sqlite3
import bcrypt


class User:
    def __init__(self, fname: str, lname: str, username: str, role: str):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.role = role
        # self.password = password
    
    @staticmethod
    def login(credentials: dict):
        con = sqlite3.connect("db/Bookstore.db")  # connect to db
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        row = cur.execute(
            f"SELECT * FROM users WHERE username LIKE \"{credentials.get('username')}\";").fetchone()
        con.close()
        if row and bcrypt.checkpw(
                credentials['password'].encode('utf-8'),
                row['password_hash'].encode('utf-8')
            ):
            return User(row['fname'], row['lname'], row['username'], row['role'])     
        else:
            print(red_text('User or password is incorrect'))

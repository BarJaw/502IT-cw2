import sqlite3
import bcrypt
from user import User

class Administrator(User):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @staticmethod
    def view_employees():
        # Connect to database
        conn = sqlite3.connect('Bookstore.db')
        # Create a cursor
        cursor = conn.cursor()

        # Query The Database
        cursor.execute("SELECT rowid, fname, lname FROM Users WHERE role = 'employee'")
        items = cursor.fetchall()

        for item in items:
            print(item)

        # Close our connection
        conn.close()
    
    @staticmethod
    def add_employee(fname: str, lname: str, username: str, password: str):
        # Connect to database
        conn = sqlite3.connect('Bookstore.db')
        # Create a cursor
        cursor = conn.cursor()

        role = "employee"
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        if Administrator.check_if_username_exists(username) == False:
            cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?)", (fname, lname, username, hashed_password, role))
        else:
            print("This username is taken")

        # Commit the changes
        conn.commit()
        # Close our connection
        conn.close()

    @staticmethod
    def remove_employee(username: str):
        # Connect to database
        conn = sqlite3.connect('Bookstore.db')
        # Create a cursor
        cursor = conn.cursor()

        if Administrator.check_if_username_exists(username):
            cursor.execute("DELETE FROM Users WHERE login = (?)", username)

        # Commit the changes
        conn.commit()
        # Close our connection
        conn.close()

    @staticmethod
    def check_if_username_exists(username: str):
        # Connect to database
        conn = sqlite3.connect('Bookstore.db')
        # Create a cursor
        cursor = conn.cursor()

        cursor.execute("SELECT username FROM Users WHERE username = (?)", username)
        username_check = cursor.fetchall()

        if len(username_check) == 0:
            return False
        else:
            return True

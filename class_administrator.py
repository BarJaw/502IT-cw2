import sqlite3
import bcrypt
from user import User

class Administrator(User):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    
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
    def add_employee(fname: str, lname: str, login: str, password: str):
        # Connect to database
        conn = sqlite3.connect('Bookstore.db')
        # Create a cursor
        cursor = conn.cursor()

        role = "employee"
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?)", (fname, lname, login, hashed_password, role))

        # Commit the changes
        conn.commit()
        # Close our connection
        conn.close()

    @staticmethod
    def remove_employee(login: str):
        # Connect to database
        conn = sqlite3.connect('Bookstore.db')
        # Create a cursor
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Users WHERE login = (?)", login)

        # Commit the changes
        conn.commit()
        # Close our connection
        conn.close()

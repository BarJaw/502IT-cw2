import sqlite3
import bcrypt
from colors import green_text, red_text, blue_text
from user import User
from prettytable import PrettyTable

class Administrator(User):
    def __init__(self, User):
        super().__init__(User.fname, User.lname, User.username, role="administrator")
    
    @staticmethod
    def view_employees():
        con = sqlite3.connect("db/Bookstore.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        cur.execute("SELECT id, fname, lname, username, role FROM Users WHERE role = 'employee' ORDER BY RANDOM();")
        column_names = [description[0] for description in cur.description]
        
        table = PrettyTable(column_names)
        table.align = 'l'
        for row in cur.fetchall():
            table.add_row(row)
        print(table)
        
        con.close()
    
    @staticmethod
    def add_employee():
        conn = sqlite3.connect('db/Bookstore.db')
        cursor = conn.cursor()

        print('Please provide the first name of the employee.')
        fname = input(blue_text('First name: '))
        while not fname:
            print(red_text('The name you provided is incorrect. Please try again.'))
            fname = input(blue_text('First name: '))
        
        print('Please provide the last name of the employee.')
        lname = input(blue_text('Last name: '))
        while not lname:
            print(red_text('The last name you provided is incorrect. Please try again.'))
            lname = input(blue_text('Last name: '))
        
        username = lname + fname[0]
        role = "employee"
        hashed_password = bcrypt.hashpw(''.encode('utf-8'), bcrypt.gensalt())
        
        try:
            if Administrator.check_if_username_exists(username) is None:
                cursor.execute("INSERT INTO Users (fname, lname, username, password_hash, role) VALUES (?, ?, ?, ?, ?)", (fname, lname, username, hashed_password, role))
                print(green_text('Employee successfully added.'))
            else:
                print(red_text("This username is taken"))
        except:
            print(red_text('Something went wrong. Please try again.'))

        conn.commit()
        conn.close()

    @staticmethod
    def remove_employee():
        conn = sqlite3.connect('db/Bookstore.db')
        cursor = conn.cursor()

        print('Please provide the username of employee you want to remove.')
        username = input(blue_text('Username: '))
        while not username:
            print(red_text('The username you provided is incorrect. Please try again.'))
            username = input(blue_text('Username: '))
            
        try:
            if Administrator.check_if_username_exists(username):
                cursor.execute("DELETE FROM Users WHERE username = ?", (username,))
            else:
                print(red_text('User with such username does not exist.'))
        except:
            print(red_text('Something went wrong. Please try again.'))
            
        conn.commit()
        conn.close()

    @staticmethod
    def check_if_username_exists(username: str):
        # Connect to database
        conn = sqlite3.connect('db/Bookstore.db')
        # Create a cursor
        cursor = conn.cursor()

        cursor.execute("SELECT username FROM Users WHERE username = ?", (username,))
        result = cursor.fetchone() 
        conn.close()
        
        return result

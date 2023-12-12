import sqlite3
from user import User  # Assuming you have a User class defined in user.py
from order import Order  # Assuming you have an Order class defined in order.py
from book import Book
from colors import red_text, green_text, blue_text
from getpass import getpass
from prettytable import PrettyTable
from utils import is_float


class Employee(User):
    def __init__(self, User):
        super().__init__(User.fname, User.lname, User.username, role="employee")

    @staticmethod
    def view_books():
        con = sqlite3.connect("db/Bookstore.db")  # connect to db
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        # SELECT RANDOM SO IT CAN BE SORTED LATER!!!!
        cur.execute(f"SELECT * FROM Books ORDER BY RANDOM();")

        # Get column names
        column_names = [description[0] for description in cur.description]

        # Display the results in a table
        table = PrettyTable(column_names)
        table.align = 'l'
        for row in cur.fetchall():
            table.add_row(row)
        print(table)
        
        con.close()

    @staticmethod
    def add_book():
        con = sqlite3.connect("db/Bookstore.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        try:
            print('Please provide the following book details.')

            book_name = input('Book title: ').strip()
            while not book_name:
                print(red_text(
                    'Book title you provided is incorrect. Please provide correct book title'))
                book_name = input('Book title: ').strip()

            # This if checks whether the book already exists in the db. If not then inserts the book, else throws an error.
            if cur.execute("SELECT name FROM Books WHERE name = (?)", (book_name,)).fetchone() is None:
                author = input('Author: ')
                while not author:
                    print(
                        red_text('Author you provided is incorrect. Please provide correct author.'))
                    author = input('Author: ')

                quantity = input('Stock: ')
                while not quantity.isdecimal() or int(quantity) < 0:
                    print(red_text(
                        'Quantity you provided is incorrect. Please provide correct quantity.'))
                    quantity = input('Stock: ')
                quantity = int(quantity)

                price = input('Price: ')
                while not price or not is_float(price) or float(price) < 0:
                    print(red_text(
                        'Price you provided is incorrect. Please provide correct price.'
                    ))
                    price = input('Price: ')
                price = float(price)

                cur.execute("INSERT INTO Books (name, author, stock, price) VALUES (?,?,?,?);",
                            (book_name, author, quantity, price))
                con.commit()
                con.close()
                print(green_text('Book successfully added'))
            else:
                print(
                    red_text('Such book already exists. Please edit the existing position.'))
        except Exception as e:
            print(red_text('Something went wrong. Please try again.'))
            print(e)

    @staticmethod
    def remove_book():
        con = sqlite3.connect("db/Bookstore.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        
        print('Please provide the book title you want to delete: ')
        book_name = input(blue_text('Book title: '))
        while not book_name:
            print(red_text('Book title you provided is incorrect. Please try again.'))
            book_name = input(blue_text('Book title: '))
        
        if cur.execute("SELECT name FROM Books WHERE name = (?)", (book_name,)).fetchone() is not None:
            cur.execute("DELETE FROM Books WHERE name = ?", (book_name,))
            con.commit()
            con.close()
            print(green_text('Book deleted successfully.'))
        else:
            print(red_text('Book with such title does not exists.'))
        
    @staticmethod
    def view_orders():
        con = sqlite3.connect("db/Bookstore.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        
        cur.execute(f"SELECT * FROM Orders ORDER BY RANDOM();") # SORTING ALGORITHM
        
        column_names = [description[0] for description in cur.description]
        
        table = PrettyTable(column_names)
        table.align = 'l'
        for row in cur.fetchall():
            table.add_row(row)
        print(table)
        
        con.close()
    
    @staticmethod
    def accept_order():
        # ALSO ADD EXCEPTIONS (check if order is waiting for acceptance and only modify those, otherwise spit an error)
        con = sqlite3.connect("db/Bookstore.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        
        print('Please provide the order id you want to accept.')
        order_id = input(blue_text('Order id: '))
        if not order_id or not order_id.isdecimal():
            print(red_text('Order id you provided is incorrect. Please try again.'))
            order_id = input(blue_text('Order id: '))
        
        if cur.execute(f"SELECT id, status FROM Orders WHERE id = ?", (order_id,)).fetchone() is None:
            print(red_text('Order with such id does not exist.'))
        
        
        
        else:
            try:
                cur.execute("UPDATE Orders SET status = 'accepted' WHERE id = ?;", (order_id))
                print(green_text('The order has been accepted.'))
            except:
                print(red_text('Something went wrong. Please try again.'))
        
        con.commit()
        con.close()
    
    @staticmethod
    def cancel_order():
        ...
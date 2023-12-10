import sqlite3
from user import User  # Assuming you have a User class defined in user.py
from order import Order  # Assuming you have an Order class defined in order.py
from book import Book
from colors import red_text, green_text, blue_text
from getpass import getpass
from prettytable import PrettyTable


class Employee(User):
    def __init__(self, User):
        super().__init__(User.fname, User.lname, User.username, role="employee")

    @staticmethod
    def view_books():
        con = sqlite3.connect("db/Bookstore.db")  # connect to db
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Books ORDER BY RANDOM();") # SELECT RANDOM SO IT CAN BE SORTED LATER!!!!

        # Get column names
        column_names = [description[0] for description in cur.description]

        # Display the results in a table
        table = PrettyTable(column_names)
        table.align = 'l'
        for row in cur.fetchall():
            table.add_row(row)
        print(table)

    @staticmethod
    def add_book():
        # INSERT INTO Books (name, author, stock, price) VALUES ('dziady cz. 1', 'mickiewicz', 10, 5.99);
        try:
            print('Please provide the following book details.')
            book_name = input('Book title: ')
            author = input('Author: ')
            quantity = int(input('Stock: '))
            price = float(input('Price: '))
            con = sqlite3.connect("db/Bookstore.db")  # connect to db
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("INSERT INTO Books (name, author, stock, price) VALUES (?,?,?,?);",
                        (book_name, author, quantity, price))
            con.commit()
            con.close()
            print(green_text('Book successfully added'))
        except:
            print(red_text('Something went wrong. Please try again'))
        
    def remove_book(self, book_id):
        # Add code to remove a book from the database
        # You can use the book's ID to identify and delete the book
        print(f"Removing book with ID: {book_id}")

    def view_orders(self):
        # Add code to retrieve and display a list of orders
        print("Viewing orders...")

    def accept_order(self, order):
        # Add code to update the order status as accepted
        print(f"Accepting order: {order}")

    def cancel_order(self, order_id):
        # Add code to cancel an order
        # You can use the order's ID to identify and update the order status
        print(f"Cancelling order with ID: {order_id}")

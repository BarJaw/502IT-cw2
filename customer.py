import sqlite3
import bcrypt
from user import User
from colors import red_text, green_text, blue_text
from getpass import getpass


class Customer(User):
    role = "customer"

    def __init__(self, User):
        super().__init__(User.fname, User.lname, User.username, self.role)
        self.cart = {}  # initializes dictionary for the cart, {book : stock_quantity}

    @staticmethod
    def register():
        print('Please provide the following information.')
        username = None
        while not username:
            username = input('Username: ')
            while not username:
                print(red_text('Please provide username'))
                username = input('Username: ')
            con = sqlite3.connect("db/Bookstore.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            row = cur.execute(
                f"SELECT * FROM users WHERE username LIKE \"{username}\";").fetchone()
            if row:
                print(red_text('Such username already exists. Please choose another.'))
                username = None

        password = getpass('Password: ')
        while not password:
            print(red_text('Please provide password'))
            password = getpass('Password: ')
        password = bcrypt.hashpw(password.encode(
            'utf-8'), bcrypt.gensalt()).decode("utf-8")

        fname = input('First name: ').capitalize()
        while not fname:
            print(red_text('Please provide your name'))
            fname = input('First name: ').capitalize()

        lname = input('Last name: ').capitalize()
        while not lname:
            print(red_text('Please provide your last name'))
            lname = input('Last name: ').capitalize()

        try:
            cur.execute(f"INSERT INTO Users (fname, lname, username, password_hash, role)\
                VALUES ('{fname}', '{lname}', '{username}', '{password}', 'customer');")
            con.commit()
            print(green_text('User registered successfuly'))
        except:
            print(red_text('Something went wrong. Please try again.'))
        con.close()

    @staticmethod
    def view_book(book):  # method to display information of the book
        print(f"Name: {book.name}",
              f"Author: {book.author}",
              f"Price: {book.price}",
              f"Stock quantity: {book.stock_quantity}")

    def add_to_cart(self, book, quantity):
        if book in book.all_books:  # 'book.all_books' is a placeholder for database with books
            if quantity > 0:
                if len(book.stock_quantity) != 0:
                    if book.stock_quantity >= quantity:  # check if the requested amount of books is available and it is more 0
                        if book not in self.cart:  # check if the book hasn't been added to the cart before
                            # could be 'book.name' instead of book object
                            self.cart.update({book: quantity})
                            book.stock_quantity -= quantity
                        else:
                            # if the book is already in the cart, update its quantity
                            self.cart[book] += quantity
                    else:
                        print("Requested amount is more than left in stock")
                else:
                    print(f"No more {book.name} left in stock")
            else:
                print("Quantity should be more than 0")
        else:
            print("No such book in the store")

    def view_cart(self):
        total_amount = 0
        if self.cart:
            print("---- My Cart ----")
            for book, quantity in self.cart.items():
                print(f"{book}: {quantity}")
            for book in self.cart:
                total_amount += book.price
            print(f"Total amount: {total_amount} EUR")
        else:
            print("Your cart is empty")

    # method to check out the cart, but we should also add method to modify the cart (e.g. delete items or their quantity)
    def check_out_cart(self):
        if self.cart:
            print("Successfully checked out")
            self.cart.clear()
        else:
            print("Your cart is empty")

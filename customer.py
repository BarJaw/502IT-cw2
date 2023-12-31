import sqlite3
import math
import bcrypt
from datetime import datetime, timedelta
from user import User
from colors import red_text, green_text, blue_text
from getpass import getpass
from prettytable import PrettyTable
from book import Book


class Customer(User):
    def __init__(self, User):
        super().__init__(User.fname, User.lname, User.username, role='customer')
        # initializes list of dictionaries for the cart, [{book : stock_quantity}]
        self.cart = []

    @staticmethod
    def register():
        print('Please provide the following information.')

        # Get user and compare with database
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

        # Check if the password hash matches
        password = getpass('Password: ')
        while not password:
            print(red_text('Please provide password'))
            password = getpass('Password: ')
        password = bcrypt.hashpw(password.encode(
            'utf-8'), bcrypt.gensalt()).decode("utf-8")

        # Get the first name
        fname = input('First name: ').capitalize()
        while not fname:
            print(red_text('Please provide your name'))
            fname = input('First name: ').capitalize()

        # Get the last name
        lname = input('Last name: ').capitalize()
        while not lname:
            print(red_text('Please provide your last name'))
            lname = input('Last name: ').capitalize()

        # Insert gathered data into database
        try:
            cur.execute(f"INSERT INTO Users (fname, lname, username, password_hash, role)\
                VALUES ('{fname}', '{lname}', '{username}', '{password}', 'customer');")
            con.commit()
            print(green_text('User registered successfuly'))
        except:
            print(red_text('Something went wrong. Please try again.'))
        con.close()

    def add_to_cart(self):
        # Connect to database
        conn = sqlite3.connect('db/Bookstore.db')
        # Create a cursor
        cursor = conn.cursor()

        book = input(blue_text("Input the name of the book: "))
        quantity = int(input(blue_text("Input the quantity: ")))
        book_quantity = cursor.execute(
            "SELECT stock FROM Books WHERE name = ?", (book,)).fetchone()[0]
        if book in cursor.execute("SELECT name FROM Books WHERE name = ?", (book,)).fetchone():
            if quantity > 0:
                if book_quantity:
                    if book_quantity >= quantity:
                        book_titles = []
                        for position in self.cart:
                            book_titles.extend(list(position.keys()))
                        if book not in book_titles:
                            self.cart.append({book: quantity})
                            print(green_text("Successfully appended."))
                        else:
                            for position in self.cart:
                                for book_name in position:
                                    if book_name == book:
                                        position[book] += quantity
                                        if position[book] > book_quantity:
                                            position[book] -= quantity
                                            print(
                                                red_text("The amount exceeds book's stock value."))
                                        else:
                                            print(green_text(
                                                "Successfully appended."))
                    else:
                        print(
                            red_text("Requested amount is more than left in stock."))
                else:
                    print(red_text(f"No more {book} left in stock."))
            else:
                print(red_text("Quantity should be more than 0."))
        else:
            print(red_text("No such book in the store."))
        # Close the connection
        cursor.close()

    def calculate_total_amount(self):
        # Connect to database
        conn = sqlite3.connect('db/Bookstore.db')
        # Create a cursor
        cursor = conn.cursor()

        total_amount = 0
        for position in self.cart:
            for book, quantity in position.items():
                book_price = cursor.execute(
                    "SELECT price FROM Books WHERE name = ?;", (book,)).fetchone()[0]
                total_amount += book_price * quantity

                # Close the connection
                cursor.close()
        return round(total_amount, 2)

    def view_cart(self):
        print(blue_text("---- My Cart ----"))
        if self.cart:
            for position in self.cart:
                for book, quantity in position.items():
                    print(f"{book}: {quantity}")
            total_amount = self.calculate_total_amount()
            print(f"Total amount: {total_amount:.2f} EUR")
        else:
            print("Your cart is empty.")

    def check_out_cart(self):
        if self.cart:
            # Connect to database
            conn = sqlite3.connect('db/Bookstore.db')
            # Create a cursor
            cursor = conn.cursor()

            city = input(
                blue_text("Please provide the city of the delivery: ")).capitalize()

            # if such city exists
            if city in cursor.execute("SELECT city FROM Cities WHERE city = ?", (city,)).fetchone()[0]:
                # street input
                street = input(
                    blue_text("Please provide the street of the delivery: "))
                # concatenate city and street into one variable
                address = f"{city}, {street}"

                order_date_str = datetime.now().strftime(
                    "%d.%m.%Y")  # current date as a string
                # convert current date into a date object
                order_date = datetime.strptime(order_date_str, "%d.%m.%Y").date()
                # get the shipment time from database
                shipment_time = cursor.execute("SELECT shipment_time FROM Cities WHERE city = ?", (city,)).fetchone()[0]  
                # calculate the estimated date of arrival
                estimated_date_of_arrival = order_date + timedelta(days=shipment_time)
                total_amount = self.calculate_total_amount()
                # calculate priority based on total amount
                if total_amount >= 100:
                    priority = 10
                elif total_amount < 10:
                    priority = 1
                else:
                    priority = math.floor(total_amount / 10)

                # status of an order
                status = "waiting for acceptance"

                # get id of the user based on his username
                my_id = cursor.execute("SELECT id FROM Users WHERE username = ?;", (self.username,)).fetchone()[0]
                total_amount = self.calculate_total_amount()

                # Add the order into the database
                cursor.execute("INSERT INTO Orders (date, priority, status, address, estimated_date_of_arrival, amount, book_list, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                               (order_date.strftime("%d.%m.%Y"), priority, status, address, estimated_date_of_arrival.strftime("%d.%m.%Y"), total_amount, f'{self.cart}', my_id,))

                # Subtract the stock quantity of the checked out books
                for position in self.cart:  # iterate through the cart
                    for book, quantity in position.items():
                        current_stock = cursor.execute("SELECT stock FROM Books WHERE name = ?", (book,)).fetchone()[0]
                        updated_stock = str(current_stock - quantity)  # updated stock number
                        # update the stock of the book
                        cursor.execute("UPDATE Books SET stock = ? WHERE name = ?", (updated_stock, book,))

                # Commit the changes to the database
                conn.commit()
                # Close the connection
                conn.close()

                print(green_text("Successfully checked out."))
                self.cart.clear()
            else:
                print(red_text(
                    "Please provide the valid city name, here is the list of similar cities:"))
                similar_cities = cursor.execute(
                    f"SELECT city FROM Cities WHERE city LIKE ?;", (f'%{city}%',)).fetchall()
                for city in similar_cities:
                    print(city)
                self.check_out_cart()

                # Close the connection
                conn.close()
        else:
            print("Your cart is empty.")

    @staticmethod
    def search_book():
        # Ask user for a book name
        book_name = input(blue_text('Please provide the book name: '))

        # Connect to database and get all books which have user input in the name field
        con = sqlite3.connect("db/Bookstore.db")  # connect to db
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM Books WHERE name LIKE ? ORDER BY RANDOM();", (f'%{book_name}%',))

        # Get column names
        column_names = [description[0] for description in cur.description]

        # Display the results in a table
        table = PrettyTable(column_names)
        table.align = 'l'
        for row in cur.fetchall():  # MAYBE APPLY SORTING HERE
            table.add_row(row)
        print(table)

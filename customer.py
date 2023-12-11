import sqlite3
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
        # initializes dictionary for the cart, {book : stock_quantity}
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

    def add_to_cart(self, book, quantity):
        # Connect to database
        conn = sqlite3.connect('db/Bookstore')
        # Create a cursor
        cursor = conn.cursor()

        book_quantity = cursor.execute("SELECT stock FROM Books WHERE name = (?)", book).fetchone()

        if book in cursor.execute("SELECT name FROM Books WHERE name = (?)", book).fetchall():
            if quantity > 0:
                if len(book_quantity) != 0:
                    if book_quantity >= quantity:  # check if the requested amount of books is available and it is more 0
                        if book not in self.cart:  # check if the book hasn't been added to the cart before
                            self.cart.append({book: quantity})
                        else:
                            for position in self.cart:
                                for book_obj in position:
                                    if book_obj == book:
                                        position[book] += quantity
                    else:
                        print("Requested amount is more than left in stock")
                else:
                    print(f"No more {book.name} left in stock")
            else:
                print("Quantity should be more than 0")
        else:
            print("No such book in the store")

        cursor.close()

    def calculate_total_amount(self):
        total_amount = 0
        for position in self.cart:
            for book, quantity in position.items():
                total_amount += book.price * quantity
        return total_amount

    def view_cart(self):
        print("---- My Cart ----")

        if self.cart:
            for position in self.cart:
                for book, quantity in position.items():
                    print(f"{book.name}: {quantity}")
            total_amount = self.calculate_total_amount()
            print(f"Total amount: {total_amount:.2f} EUR")
        else:
            print("Your cart is empty")

    def check_out_cart(self):
        priority = "high"
        status = "in progress"

        if self.cart:
            # Connect to database
            conn = sqlite3.connect('db/Bookstore')
            # Create a cursor
            cursor = conn.cursor()

            city = input("Please provide the city of the delivery: ").capitalize()

            if city in cursor.execute(f"SELECT city FROM Cities WHERE city = {city}").fetchall(): # if such city exists
                street = input("Please provide the street of the delivery: ") # street input
                address = f"City: {city}, Street: {street}" # concatenate city and street into one variable

                order_date_str = datetime.now().strftime("%d.%m.%Y") # current date as a string
                order_date = datetime.strptime(order_date_str, "%d.%m.%Y") # convert current date into a date object
                shipment_time = cursor.execute(f"SELECT shipment_time FROM Cities WHERE city = {city}").fetchone() # get the shipment time from database
                estimated_date_of_arrival = order_date + timedelta(days=shipment_time) # calculate the estimated date of arrival

                my_id = cursor.execute(f"SELECT id FROM Users WHERE username = {self.username}").fetchone() # get id of the user based on his username

                amount = self.calculate_total_amount()

                # Add the order into the database
                cursor.execute("INSERT INTO Orders VALUES (?, ?, ?, ?, ?, ?)",
                            (order_date, priority, status, address, estimated_date_of_arrival, amount, self.cart, my_id))

                # Subtract the stock quantity of the checked out books
                for position in self.cart:  # iterate through the cart
                    for book, quantity in position.items():
                        current_stock = cursor.execute(f"SELECT stock FROM Books WHERE name = {book.name}").fetchone() # current stock of the book
                        updated_stock = current_stock - quantity # updated stock number
                        cursor.executemany(f"UPDATE Books SET stock = {updated_stock} WHERE name = {book.name}") # update the stock of the book

                # Commit the changes to the database
                conn.commit()
                # Close the connection
                conn.close()

                print("Successfully checked out")
                self.cart.clear()
            else:
                print("Please provide the valid city name, here is the list of similar cities:")
                similar_cities = cursor.execute(f"SELECT city WHERE city LIKE '%{city}%'").fetchall()
                for city in similar_cities:
                    print(city)
                self.check_out_cart()

                # Close the connection
                conn.close()
        else:
            print("Your cart is empty")

    @staticmethod
    def search_book():
        # Ask user for a book name
        book_name = input(blue_text('Please provide the book name: '))

        # Connect to database and get all books which have user input in the name field
        con = sqlite3.connect("db/Bookstore.db")  # connect to db
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Books WHERE name LIKE '%{book_name}%';")

        # Get column names
        column_names = [description[0] for description in cur.description]

        # Display the results in a table
        table = PrettyTable(column_names)
        table.align = 'l'
        for row in cur.fetchall():  # MAYBE APPLY SORTING HERE
            table.add_row(row)
        print(table)

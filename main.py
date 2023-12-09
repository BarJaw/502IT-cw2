from customer import Customer
from order import Order
from book import Book
from user import User
from colors import blue_text, green_text, red_text

import sqlite3
import bcrypt


class System():
    @staticmethod
    def main():
        while True:
            System.view_initial_menu()

    @staticmethod
    def view_initial_menu():
        print("""\n1. Register\n2. Login\n3. Exit""")
        choice = input(blue_text("Choose an option: "))

        if choice == "1":
            return User.login('Bartosz', 'Jaworski')
            ... # login
        elif choice == "2":
            return Customer.register()
            ...
        elif choice == "3":
            exit(1)
        else:
            print(red_text("Invalid choice. Please choose again"))


if __name__ == '__main__':
    System.main()

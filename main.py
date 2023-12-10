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
    def get_credentials() -> dict:
        creds = {
            'username': input('Username: '),
            'password': input('Password: ')
        }
        return creds
    
    @staticmethod
    def view_initial_menu():
        print("\n1. Login\n2. Register\n3. Exit")
        choice = input(blue_text("Choose an option: "))
        match choice:
            case "1":
                credentials = System.get_credentials()
                user = User.login(credentials)
                match user.role:
                    case 'customer':
                        user = Customer(user)
                        print('Logged in as customer!')
                        return user
                    case 'employee':
                        ...
                        # user = Employee(user)
                    case 'administrator':
                        ...
                        # user = Administrator(user)
            case "2":
                ...
                return Customer.register()
            case "3":
                exit(1)
            case _:
                print(red_text("Invalid choice. Please choose again"))

    
if __name__ == '__main__':
    System.main()

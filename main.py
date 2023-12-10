from customer import Customer
from order import Order
from book import Book
from user import User
from colors import blue_text, green_text, red_text
from getpass import getpass
import sqlite3
import bcrypt


class System():
    @staticmethod
    def main():
        user = User('Bartosz', 'Jaworski', 'barjaw', 'customer')
        while not user:
            user = System.view_initial_menu()

        if user.role == 'customer':
            customer = Customer(user)
            System.view_customer_menu(customer)
        elif user.role == 'employee':
            ...  # do employee stuff
        elif user.role == 'administrator':
            ...  # do admin stuff

    @staticmethod
    def get_credentials() -> dict:
        creds = {
            'username': input('Username: '),
            'password': getpass('Password: ')
        }
        return creds

    @staticmethod
    def view_initial_menu():
        print('\n1. Login\n2. Register\n3. Exit')
        choice = input(blue_text('Choose an option: '))
        match choice:
            case '1':
                credentials = System.get_credentials()
                user = User.login(credentials)
                if user:
                    match user.role:
                        case 'customer':
                            user = Customer(user)
                            print(green_text(f'Logged in as {user.username}!'))
                            return user
                        case 'employee':
                            ...
                            # user = Employee(user)
                        case 'administrator':
                            ...
                            # user = Administrator(user)
            case '2':
                Customer.register()
            case '3':
                exit(1)
            case _:
                print(red_text('Invalid choice. Please choose again'))

    @staticmethod
    def view_customer_menu(customer):
        print('1. Search for a book\n2. View book details\n3. Add book to cart\n4. Checkout \n5. View account details \n6. Change account details\n7. Exit \n')
        choice = input(blue_text('Choose an option: '))
        match choice:
            case '1':
                customer.search_book()
            case '2':
                ...
            case '3':
                ...
            case '4':
                ...
            case '5':
                ...
            case '6':
                ...
            case '7':
                exit(1)
            case _:
                print(red_text('Invalid choice. Please choose again'))


if __name__ == '__main__':
    System.main()

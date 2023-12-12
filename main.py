from banner import banner
from customer import Customer
from employee import Employee
from administrator import Administrator
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
        banner()
        user = User('Bartosz', 'Jaworski', 'barjaw', 'customer')
        while not user:
            user = System.view_initial_menu()

        if user.role == 'customer':
            customer = Customer(user)
            while True:
                System.view_customer_menu(customer)
        elif user.role == 'employee':
            employee = Employee(user)
            while True:
                System.view_employee_menu()
        elif user.role == 'administrator':
            administrator = Administrator(user)
            while True:
                pass
                # System.view_administrator_menu()

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
                            user = Employee(user)
                            print(green_text(f'Logged in as {user.username}!'))
                            return user
                        case 'administrator':
                            user = Administrator(user)
                            print(green_text(f'Logged in as {user.username}!'))
                            return user
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
                Customer.search_book()
            case '2':
                ...
            case '3':
                customer.add_to_cart()
            case '4':
                Customer.check_out_cart()
            case '5':
                ...
            case '6':
                ...
            case '7':
                exit(1)
            case _:
                print(red_text('Invalid choice. Please choose again'))

    @staticmethod
    def view_employee_menu():
        print('1. View books\n2. Add book to database\n3. Delete book from database\n4. View orders\n5. Accept order\n6. Cancel order\n7. Exit \n')
        choice = input(blue_text('Choose an option: '))
        match choice:
            case '1':
                Employee.view_books()
            case '2':
                Employee.add_book()
            case '3':
                Employee.remove_book()
            case '4':
                Employee.view_orders()
            case '5':
                Employee.accept_order()
            case '6':
                Employee.cancel_order()
            case '7':
                exit(1)
            case _:
                print(red_text('Invalid choice. Please choose again'))


if __name__ == '__main__':
    System.main()

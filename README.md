# Bookstore Project

## Description

The Bookstore project is a simple command-line application for managing a bookstore. It allows users to log in as customers, employees, or administrators, perform various tasks such as searching for books, viewing details, adding books to the cart, checking out, managing book inventory, handling orders, and administering employee accounts.

## Features

- **User Authentication:** Users can register an account or log in as customers, employees, or administrators.
- **Customer Features:**
  - Search for books
  - View book details
  - Add books to the cart
  - Checkout
  - View account details
  - Change account details

- **Employee Features:**
  - View all books
  - Add a new book to the database
  - Delete a book from the database
  - View orders
  - Accept orders

- **Administrator Features:**
  - View employees
  - Add an employee
  - Remove an employee
  - Check if a username exists

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/bookstore.git
   cd bookstore
   ```

2. Install Dependencies:

   ```bash 
   pip install prettytable
   pip install bcrypt
   pip install sqlite3
   ```

3. Run the Application:

    ```bash
    python main.py
    ```

## Usage
1.Start the application by running main.py.
2.Follow the on-screen prompts to log in or register.
3.Depending on the user role (customer, employee, administrator), navigate through the available menu options.
4.Perform various tasks such as searching for books, managing the cart, viewing orders, administering employees, etc.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
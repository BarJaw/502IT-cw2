from datetime import date

class Order:
    def __init__(self, order_id, order_date, priority, status, address, book_list, user_id):
        self.id = order_id
        self.date = order_date
        self.priority = priority
        self.status = status
        self.address = address
        self.book_list = book_list  # Assuming book_list is a dictionary {book_id: quantity}
        self.user_id = user_id

    def display_order_details(self):
        print(f"Order ID: {self.id}")
        print(f"Order Date: {self.date}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")
        print(f"Address: {self.address}")
        print("Book List:")
        for book_id, quantity in self.book_list.items():
            print(f"  Book ID: {book_id}, Quantity: {quantity}")
        print(f"User ID: {self.user_id}")

class Book:
    def __init__(self, book_id, name, author, stock, price):
        self.id = book_id
        self.name = name
        self.author = author
        self.stock = stock
        self.price = price

    def edit_quantity(self, new_quantity):
        self.stock = new_quantity

    def display_book_details(self):
        print(f"Book ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Stock: {self.stock}")
        print(f"Price: ${self.price:.2f}")

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

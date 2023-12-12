from datetime import datetime

class Book:
    def __init__(self, book_id, title, price):
        self.book_id = book_id
        self.title = title
        self.price = price

class Order:
    def __init__(self, order_id, delivery_address):
        self.order_id = order_id
        self.date = datetime.now()
        self.status = "Pending"
        self.delivery_address = delivery_address
        self.books = []

    def add_book(self, book, quantity=1):
        for _ in range(quantity):
            self.books.append(book)

    def get_ordered_books(self):
        return self.books

# Function for customers to check the list of ordered books
def check_ordered_books(order):
    ordered_books = order.get_ordered_books()
    if ordered_books:
        print("List of Ordered Books:")
        for book in ordered_books:
            print(f"- {book.title}")
    else:
        print("No books ordered.")

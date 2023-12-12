class Book:
    def __init__(self, book_id, name, author, stock, price):
        self.id = book_id
        self.name = name
        self.author = author
        self.stock = stock
        self.price = price

    def edit_quantity(self, new_quantity):
        self.stock = new_quantity

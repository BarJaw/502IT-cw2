class Book:
    def __init__(self, book_id, name, author, stock, price):
        self.id = book_id
        self.name = name
        self.author = author
        self.stock = stock
        self.price = price

    def edit_quantity(self, quantity_change):
        # Adjust the stock by adding the quantity_change
        self.stock += quantity_change

# Placeholder class
class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.login = None
        self.password = None


class Customer(User):
    role = "customer"

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.cart = {}  # initializes dictionary for the cart, {book : stock_quantity}

    @staticmethod
    def view_book(book):  # method to display information of the book
        print(f"Name: {book.name}",
              f"Author: {book.author}",
              f"Price: {book.price}",
              f"Stock quantity: {book.stock_quantity}")

    def add_to_cart(self, book, quantity):
        if book in book.all_books:  # 'book.all_books' is a placeholder for database with books
<<<<<<< HEAD
            if quantity > 0:
                if len(book.stock_quantity) != 0:
                    if book.stock_quantity >= quantity:  # check if the requested amount of books is available and it is more 0
                        if book not in self.cart:  # check if the book hasn't been added to the cart before
                            self.cart.update({book: quantity})  # could be 'book.name' instead of book object
                            book.stock_quantity -= quantity
                        else:
                            self.cart[book] += quantity  # if the book is already in the cart, update its quantity
                    else:
                        print("Requested amount is more than left in stock")
=======
            if book.stock_quantity >= quantity:  # check if the requested amount of books is available
                if book not in self.cart:  # check if the book hasn't been added to the cart before
                    self.cart.update({book: quantity})  # could be 'book.name' instead of book object
                    book.stock_quantity -= quantity
>>>>>>> c68edfc7cae7705cf7e9598e1b5fa139cbc53cbf
                else:
                    print(f"No more {book.name} left in stock")
            else:
                print("Quantity should be more than 0")
        else:
            print("No such book in the store")

    def view_cart(self):
        total_amount = 0
        if self.cart:
            print("---- My Cart ----")
            for book, quantity in self.cart.items():
                print(f"{book}: {quantity}")
            for book in self.cart:
                total_amount += book.price
            print(f"Total amount: {total_amount} EUR")
        else:
            print("Your cart is empty")
            
    def check_out_cart(self):  # method to check out the cart, but we should also add method to modify the cart (e.g. delete items or their quantity)
        if self.cart:
            print("Successfully checked out")
            self.cart.clear()
        else:
            print("Your cart is empty")

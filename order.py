from datetime import date


class Order:
    def __init__(self,
                 order_id: int,
                 order_date: date,
                 priority: str,
                 status: str,
                 address: str,
                 book_list: dict,
                 user_id: int
                 ):
        self.id = order_id
        self.date = order_date
        self.priority = priority
        self.status = status
        self.address = address
        # Assuming book_list is a dictionary {book_id: quantity}
        self.book_list = book_list
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

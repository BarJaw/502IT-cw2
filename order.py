from datetime import date


class Order:
    def __init__(self,
                 order_id: int,
                 order_date: date,
                 priority: str,
                 status: str,
                 address: str,
                 estimated_date_of_arrival: str,
                 book_list: dict,
                 user_id: int
                 ):
        self.id = order_id
        self.date = order_date
        self.priority = priority
        self.status = status
        self.address = address    
        self.estimated_date_of_arrival = estimated_date_of_arrival
        self.book_list = book_list
        self.user_id = user_id
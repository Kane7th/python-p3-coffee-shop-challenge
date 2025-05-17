from .order import Order

class Customer:
    def __init__(self, name):
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self.name = name
        self.orders = []

    def add_order(self, coffee, price):
        order = Order(self, coffee, price)
        self.orders.append(order)

    def __str__(self):
        return f"Customer name is: {self.name}"

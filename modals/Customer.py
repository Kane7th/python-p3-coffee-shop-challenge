from .Order import Order

class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name
        self.orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be between 1 and 15 characters.")
        

    def add_order(self, coffee, price):
        order = Order(self, coffee, price)
        self.orders.append(order)

    def __str__(self):
        return f"Customer name is: {self.name}"
    
# print(Customer("John Doe"))
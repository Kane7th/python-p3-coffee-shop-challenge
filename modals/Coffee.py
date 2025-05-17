class Coffee:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
        self.orders = []

    def __str__(self):
        return f"Coffee name is: {self.name} and price is: £{self.price:.2f}"
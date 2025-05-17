class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    def __str__(self):
        return f"Order for {self.customer.name}: {self.coffee.name} at ${self.price:.2f}"

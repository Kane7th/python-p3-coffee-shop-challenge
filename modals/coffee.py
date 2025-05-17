class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Coffee: {self.name}, Price: ${self.price:.2f}"

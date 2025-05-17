from datetime import datetime

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.timestamp = datetime.now()

        #Adds the order to the related customer and coffee
        customer.orders.append(self)
        coffee.orders.append(self)

    
    def __str__(self):
        return f"Order: {self.customer.name} ordered {self.coffee.name} for ${self.price:.2f} at {self.timestamp}"
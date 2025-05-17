class Order:
    def __init__(self, customer, coffee, price): # constructor to initialize the order
        self.customer = customer # sets the customer using the setter
        self.coffee = coffee # sets the coffee using the setter
        self.price = price # sets the price using the setter

    def __str__(self): # string representation of the order
        # returns the name of the customer and the coffee name with price
        return f"Order for {self.customer.name}: {self.coffee.name} at ${self.price:.2f}" 
    
    
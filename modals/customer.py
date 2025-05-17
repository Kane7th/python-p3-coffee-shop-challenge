from .order import Order # Importing the Order class from order module

class Customer:  # Customer class to represent a customer
    def __init__(self, name): # constructor to initialize the customer
        self.name = name # sets the name using the setter
        self.orders = [] # initializes an empty list of orders


    @property  # getter simply returns the stored '_name'
    def name(self): # returns the name of the customer
        return self._name # returns the stored name in private variable
    

    @name.setter  # checks type and length, raising errors if invalid
    def name(self, value):
        if not isinstance(value, str): # checks if value is a string
            raise ValueError("Name must be a string value")
        if not (1 <= len(value) <= 15): # checks if length is between 1 and 15
            raise ValueError("Name must be at least 3 characters long")
        self._name = value  # actual value is stored in self._name


    def add_order(self, coffee, price):   # method to add an order 
        order = Order(self, coffee, price) # creates an order object
        self.orders.append(order) # adds order to the list of orders

    def __str__(self): # string representation of the customer
        return f"Customer name is: {self.name}" # returns the name of the customer

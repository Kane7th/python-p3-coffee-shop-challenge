from .order import Order # Importing the Order class from order module

class Customer:  # Customer class to represent a customer
    def __init__(self, name): # constructor to initialize the customer
        self.name = name # calls the setter and validates the name on object creation.
        self.orders = [] # initializes an empty list of orders


    @property  # getter simply returns the stored '_name'
    def name(self): # returns the name of the customer
        return self._name # returns the stored name in private variable
    

    @name.setter  # checks type and length, raising errors if invalid
    def name(self, value):
        if not isinstance(value, str): # checks if value is a string
            raise TypeError("Name must be a string value")
        if not (1 <= len(value) <= 15): # checks if length is between 1 and 15
            raise TypeError("Name must be between 1 and 15 characters long")
        self._name = value  # actual value is stored in self._name

    def add_order(self, coffee, price):   # method to add an order 
        order = Order(self, coffee, price) # creates an order object
        self.orders.append(order) # adds order to the list of orders

    def orders(self): # returns all orders for this customer
        from .order import Order # import locally to avoid circular import
        return [order for order in Order.all_orders if order.customer == self]
    # returns all orders for this customer as a list

    def coffees(self): # returns all coffees ordered by this customer as a list 
        return list({order.coffee for order in self.orders()})
    # {order.coffee for ...} builds a set (to ensure uniqueness) & list(...) converts it to a list

    def __str__(self): # string representation of the customer
        return f"The next Customer is: {self.name}" # returns the name of the customer
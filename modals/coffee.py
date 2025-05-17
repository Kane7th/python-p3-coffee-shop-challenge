class Coffee:
    def __init__(self, name): # constructor to initialize the coffee
        self.name = name # calls the setter to set the name

    @property  # getter simply returns the stored '_name'
    def name(self): # returns the name of the coffee
        return self._name # returns the stored name in private variable
    

    @name.setter  # checks type and length, raising errors if invalid
    def name(self, value): 
        if not isinstance(value, str): # checks if value is a string
            raise TypeError("Coffee name must be a string value")
        if len(value) < 3: # checks if length is at least 3
            raise TypeError("Coffee name must be at least 3 characters long")
        self._name = value  # actual value is stored in self._name

    def orders(self):
        from .order import Order # import locally to avoid circular import
        return [order for order in Order.all_orders if order.coffee == self] 
    # returns all orders for this coffee as a list
    
    def customers(self):
        return list({order.customer for order in self.orders()}) 
    # {order.customer for ...} builds a set (to ensure uniqueness) & list(...) converts it to a list
    

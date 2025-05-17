from .order import Order # Importing the Order class from order module

class Customer:  # Customer class to represent a customer
    def __init__(self, name): # constructor to initialize the customer
        self.name = name # calls the setter and validates the name on object creation.

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

    def create_order(self, coffee, price):  # 
        from .order import Order  # import locally to avoid circular import
        return Order(self, coffee, price)

    def orders(self): # returns all orders for this customer
        from .order import Order # import locally to avoid circular import
        return [order for order in Order.all_orders if order.customer == self] 
    # single source of truth rather than using a class variable
    # returns all orders for customer as a list

    def coffees(self): # returns all coffees ordered by this customer as a list 
        return list({order.coffee for order in self.orders()})
    # {order.coffee for ...} builds a set (to ensure uniqueness) & list(...) converts it to a list

    @classmethod
    def most_aficionado(cls, coffee): # returns the customer who ordered the most of this coffee
        from .order import Order # import locally to avoid circular import

        customer_spending = {} # dictionary to store customer spending

        for order in Order.all_orders: # iterating through all orders
            if order.coffee == coffee: # checks if the coffee is the same
                customer = order.customer # gets the customer of the order
                customer.spending = customer_spending.get(customer, 0) + order.price 
                # adds the price of the order to the customer's spending

        if not customer_spending: # checks if there are no orders
            return None # returns None if there are no orders

        return max(customer_spending, key=customer_spending.get)
    # key is the function to be called on each element of the iterable
    # max() returns the maximum value of the iterable, which is the customer with the highest spending



    def __str__(self): # string representation of the customer
        return f"\nThe next Customer is: {self.name}" # returns the name of the customer
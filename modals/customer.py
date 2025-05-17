from .order import Order # Importing the Order class from order module
from .exceptions import CustomerValidationError # Importing the custom exception class for validation errors

class Customer:  # Customer class to represent a customer
    def __init__(self, name): # constructor to initialize the customer
        self.name = name # calls the setter and validates the name on object creation.

    @property  # getter simply returns the stored '_name'
    def name(self): # returns the name of the customer
        return self._name # returns the stored name in private variable
    

    @name.setter
    def name(self, value): # sets the name of the customer
        if not isinstance(value, str): # checks if value is a string
            raise CustomerValidationError("Name must be a string") # imports CustomerValidationError as a custom exception
        if not value.strip(): # checks if name is empty or whitespace
            raise CustomerValidationError("Name cannot be empty or whitespace") # imports CustomerValidationError from exceptions
        if not (1 <= len(value) <= 15): # checks if length is between 1 and 15
            raise CustomerValidationError("Name must be between 1 and 15 characters") # imports CustomerValidationError from exceptions
        self._name = value.strip() # sets the name using the setter

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
                customer_spending[customer] = customer_spending.get(customer, 0) + order.price
                # adds the price of the order to the customer's spending

        if not customer_spending: # checks if there are no orders
            return None # returns None if there are no orders

        max_spent = max(customer_spending.values()) # gets the maximum spending per customer
        top_spenders = [customer for customer, spent in customer_spending.items() if spent == max_spent] 
        # creates a list of customers who spent the most

        return top_spenders # returns the list of customers who spent the most



    def __str__(self): # string representation of the customer
        return f"\nThe next Customer is: {self.name}" # returns the name of the customer
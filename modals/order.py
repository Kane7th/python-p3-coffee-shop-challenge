from .exceptions import OrderValidationError # Importing the custom exception class for validation errors

class Order:
    all_orders = []  # class variable to store all orders

    def __init__(self, customer, coffee, price): # constructor to initialize the order
        self.customer = customer # sets the customer using the setter
        self.coffee = coffee # sets the coffee using the setter
        self.price = price # sets the price using the setter
        Order.all_orders.append(self) # adds the order to the list of orders


    @property  # getter simply returns the stored '_customer'
    def customer(self): # returns the customer of the order
        return self._customer # returns the stored customer in private variable
    
    @customer.setter  # checks type and length, raising errors if invalid
    def customer(self, value): # sets the customer of the order
        from .customer import Customer  # import locally to avoid circular import
        if not isinstance(value, Customer): # checks if value is a Customer object
            raise OrderValidationError("Customer must be a Customer object") # imports OrderValidationError as a custom exception
        self._customer = value # sets the customer using the setter
    # setter for customer, checks type and length, raising errors if invalid


    @property  # getter simply returns the stored '_coffee'
    def coffee(self): # returns the coffee of the order
        return self._coffee # returns the stored coffee in private variable
    
    @coffee.setter  # checks type and length, raising errors if invalid
    def coffee(self, value): # sets the coffee of the order
        from .coffee import Coffee  # import locally to avoid circular import
        if not isinstance(value, Coffee):
            raise OrderValidationError("Coffee must be a Coffee object") # checks if value is a Coffee object
        self._coffee = value # sets the coffee using the setter
    # setter for coffee, checks type and length, raising errors if invalid


    @property  # getter simply returns the stored '_price'
    def price(self): # returns the price of the order
        return self._price # returns the stored price in private variable
    
    @price.setter
    def price(self, value): # sets the price of the order
        try:
            price = float(value) # converts value to float
        except (TypeError, ValueError): # checks if value is a number
            raise OrderValidationError("Price must be a number") # checks if value is a number
        
        if not (1.0 <= price <= 10.0): # checks if price is between 1.0 and 10.0
            raise OrderValidationError("Price must be between 1.0 and 10.0") # checks if price is between 1.0 and 10.0
        
        self._price = round(price, 2)  # Store with 2 decimal places


    def __str__(self): # string representation of the order
        return f"{self.customer.name} has ordered: {self.coffee.name} at £{self.price:.2f}" 
    # returns the name of the customer and the coffee name with price
    

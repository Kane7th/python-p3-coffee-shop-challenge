from .modals.customer import Customer
from .modals.coffee import Coffee
from .modals.order import Order
from .modals.exceptions import ValidationError


# This is a simple script to demonstrate the usage of the Customer, Coffee, and Order classes
# The script creates a customer, adds an order for a coffee, and prints the details of the customer and their orders.
# The script is structured to be run as a standalone program, and it will not execute if imported as a module.

def main(): 
    john = Customer("John Doe") # Creating a Customer object
    latte = Coffee("Latte") # Creating a Coffee object

    brad = Customer("Brad Pitt") # Creating another Customer object
    cappuccino = Coffee("Cappuccino") # Creating another Coffee object

    chris = Customer("Chris Evans") # Creating another Customer object
    espresso = Coffee("Espresso") # Creating another Coffee object

    kane = Customer("Kane Kabena") # Creating another Customer object
    latte = Coffee("Latte") # Creating another Coffee object

    order1 = john.create_order(latte, 4.50) # this will create John's order object including the coffee and price
    order2 = brad.create_order(cappuccino, 5.00) # this will create Brad's order object including the coffee and price
    order3 = chris.create_order(espresso, 3.50) # this will create Chris's order object including the coffee and price
    order4 = kane.create_order(latte, 4.00) # this will create Kane's order object including the coffee and price
    order5 = john.create_order(latte, 5.50) # this will create John's order object including the coffee and price

 # Prints the details of customers and their orders
    print(john)
    for order in john.orders():
        print(order)

    print(brad) 
    for order in brad.orders():  
        print(order)

    print(chris)  
    for order in chris.orders():  
        print(order)

    print(kane) 
    for order in kane.orders(): 
        print(order)

    print(john) 
    for order in john.orders():  
        print(order)
    
# Prints the details of coffees and number of times it has been ordered and the average price
    print(f"\nLatte has been ordered {latte.num_orders()} times.")
    print(f"Average price for Latte: £{latte.average_price():.2f}")

    aficionados = Customer.most_aficionado(latte) # this will return the customer who ordered the most of this coffee

    if aficionados is None: # checks if there are no orders
        print("\nNo aficionado found for Latte.") # returns None if there are no orders
    elif len(aficionados) == 1: # checks if there is only one aficionado
        print(f"\nThe most aficionado for Latte is {aficionados[0].name}") # returns the name of the aficionado
    else: # checks if there is a tie
        names = ', '.join(customer.name for customer in aficionados) # creates a list of names who spent the most
        print(f"\nThere is a tie for the most aficionado for Latte among: {names}") # returns the names of the aficionados



 # Edge case 1: Coffee with no orders

    mocha = Coffee("Mocha")  # No orders created for mocha
    
    print(f"\nMocha has been ordered {mocha.num_orders()} times.") # returns the number of orders for mocha
    print(f"Average price for Mocha: £{mocha.average_price():.2f}") # returns the average price for mocha
 
    aficionado_mocha = Customer.most_aficionado(mocha) # this will return the customer who ordered the most of this coffee
    if aficionado_mocha: # checks if there is an aficionado
        print(f"The most aficionado for Mocha is {aficionado_mocha.name}") # returns the name of the aficionado
    else: # checks if there is no aficionado
        print("No aficionado found for Mocha.") # returns None if there are no orders




 # Edge case 2: Tie in spending

    order6 = chris.create_order(cappuccino, 5.00)  # same price as brad's order
    # Now brad and chris each spent 5.00 on cappuccino
    

    aficionados_cappuccino = Customer.most_aficionado(cappuccino) # this will return the customer who ordered the most of this coffee
    if aficionados_cappuccino: # checks if there is an aficionado
        if len(aficionados_cappuccino) == 1: # checks if there is only one aficionado
           print(f"\nThe most aficionado for Cappuccino is {aficionados_cappuccino[0].name}") # returns the name of the aficionado
        else: # checks if there is a tie
            names = ', '.join(cust.name for cust in aficionados_cappuccino) # creates a list of names who spent the most
            print(f"\nThere is a tie for the most aficionado for Cappuccino among: {names}") # returns the names of the aficionados
    else: # checks if there is no aficionado
        print("No aficionado found for Cappuccino.") # returns None if there are no orders


# Edge case 3: Error Handling

    try:
        # Test invalid customer name
        invalid_customer = Customer("")  # This will raise an exception
    except ValidationError as e:
        print(f"Error creating customer: {e}")

    try:
        # Test invalid coffee name
        invalid_coffee = Coffee("A")  # This will raise an exception
    except ValidationError as e:
        print(f"Error creating coffee: {e}")

    try:
        # Test invalid order
        valid_customer = Customer("Valid Name")
        valid_coffee = Coffee("Valid Coffee")
        invalid_order = Order(valid_customer, valid_coffee, 0.5)  # Price too low
    except ValidationError as e:
        print(f"Error creating order: {e}")


if __name__ == "__main__": # checks if the script is being run directly
    main() # calls the main function to run the script
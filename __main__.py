from .modals import Customer, Coffee

# This is a simple script to demonstrate the usage of the Customer, Coffee, and Order classes
# The script creates a customer, adds an order for a coffee, and prints the details of the customer and their orders.
# The script is structured to be run as a standalone program, and it will not execute if imported as a module.

def main(): 
    john = Customer("John Doe") # Creating a Customer object
    latte = Coffee("Latte") # Creating a Coffee object

    brad = Customer("Brad Pitt") # Creating another Customer object
    cappuccino = Coffee("Cappuccino") # Creating another Coffee object

    order1 = john.create_order(latte, 4.50) # this will create John's order object including the coffee and price
    order2 = brad.create_order(cappuccino, 5.00) # this will create Brad's order object including the coffee and price

    print(john)  # Printing the customer details
    for order in john.orders():  # ✅ Call the method
        print(order)

    print(brad)  # Printing the customer details
    for order in brad.orders():  # ✅ Call the method
        print(order)

if __name__ == "__main__": # This ensures that the main function is called only when this script is run directly
    main() # Calling the main function to execute the code

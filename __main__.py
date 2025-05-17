from .modals import Customer, Coffee

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
    
    print(f"\nLatte has been ordered {latte.num_orders()} times.")
    print(f"Average price for Latte: £{latte.average_price():.2f}")

    aficionado = Customer.most_aficionado(latte)
    if aficionado:
        print(f"\nThe most aficionado for Latte is {aficionado.name}")
    else:
        print("\nNo aficionado found for Latte.")


 # Edge case 1: Coffee with no orders

    mocha = Coffee("Mocha")  # No orders created for mocha
    
    print(f"\nMocha has been ordered {mocha.num_orders()} times.")
    print(f"Average price for Mocha: £{mocha.average_price():.2f}")
    aficionado_mocha = Customer.most_aficionado(mocha)
    if aficionado_mocha:
        print(f"The most aficionado for Mocha is {aficionado_mocha.name}")
    else:
        print("No aficionado found for Mocha.")

 # Edge case 2: Tie in spending

    # Add orders to create a tie for cappuccino between brad and chris
    order6 = chris.create_order(cappuccino, 5.00)  # same price as brad's order
    # Now brad and chris each spent 5.00 on cappuccino
    
    aficionados_cappuccino = Customer.most_aficionado(cappuccino)
    if aficionados_cappuccino:
        if len(aficionados_cappuccino) == 1:
           print(f"\nThe most aficionado for Cappuccino is {aficionados_cappuccino[0].name}")
        else:
            names = ', '.join(cust.name for cust in aficionados_cappuccino)
            print(f"\nThere is a tie for the most aficionado for Cappuccino among: {names}")
    else:
        print("No aficionado found for Cappuccino.")


if __name__ == "__main__":
    main()
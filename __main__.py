from .modals import Customer, Coffee

def main():
    john = Customer("John Doe")
    latte = Coffee("Latte", 4.50)

    john.add_order(latte, latte.price)

    print(john)
    for order in john.orders:
        print(order)

if __name__ == "__main__":
    main()

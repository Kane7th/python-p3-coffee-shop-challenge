import pytest
from modals.order import Order
from modals.customer import Customer
from modals.coffee import Coffee
from modals.exceptions import OrderValidationError

def setup_function():
    # Clear orders before each test
    Order.all_orders = []

def test_valid_order_creation():
    customer = Customer("Luna") # Create a customer object
    coffee = Coffee("Cappuccino") # Create a coffee object
    order = Order(customer, coffee, 3.5) # Create an order object

    assert isinstance(order, Order) # Check if order is an instance of Order
    assert order.customer == customer # Check if order's customer is the same as the one created
    assert order.coffee == coffee # Check if order's coffee is the same as the one created
    assert order.price == 3.5 # Check if order's price is the same as the one created
    assert order in Order.all_orders # Check if order is in the list of all orders

def test_customer_must_be_customer_object():
    # Create a coffee object
    coffee = Coffee("Mocha")
    with pytest.raises(OrderValidationError): # Check if error is raised
        Order("NotACustomer", coffee, 3.5) # Create an order with a string instead of a customer object

def test_coffee_must_be_coffee_object(): # Check if error is raised
    customer = Customer("Jake") # Create a customer object
    with pytest.raises(OrderValidationError): # Check if error is raised
        Order(customer, "NotACoffee", 4.0) # Create an order with a string instead of a coffee object

def test_price_must_be_number(): # Check if error is raised
    customer = Customer("Nia") # Create a customer object 
    coffee = Coffee("Flat White") # Create a coffee object
    with pytest.raises(OrderValidationError): # Check if error is raised
        Order(customer, coffee, "not_a_number") # Create an order with a string instead of a number

def test_price_must_be_in_range(): # Check if error is raised
    customer = Customer("Leo") # Create a customer object
    coffee = Coffee("Macchiato") # Create a coffee object

    with pytest.raises(OrderValidationError): # Check if error is raised
        Order(customer, coffee, 0.5)  # Below 1.0

    with pytest.raises(OrderValidationError): # Check if error is raised
        Order(customer, coffee, 10.5)  # Above 10.0

def test_price_rounds_to_two_decimals(): # Check if price rounds to two decimals
    customer = Customer("Eve") 
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 4.567)
    assert order.price == 4.57

def test_str_representation(): # Check if string representation is correct
    customer = Customer("Zoe")
    coffee = Coffee("Americano")
    order = Order(customer, coffee, 2.0)
    assert str(order) == "Zoe has ordered: Americano at £2.00"

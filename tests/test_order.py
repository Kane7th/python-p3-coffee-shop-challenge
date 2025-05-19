import pytest
from modals.order import Order
from modals.customer import Customer
from modals.coffee import Coffee
from modals.exceptions import OrderValidationError

def setup_function():
    # Clear orders before each test
    Order.all_orders = []

def test_valid_order_creation():
    customer = Customer("Luna")
    coffee = Coffee("Cappuccino")
    order = Order(customer, coffee, 3.5)

    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5
    assert order in Order.all_orders

def test_customer_must_be_customer_object():
    coffee = Coffee("Mocha")
    with pytest.raises(OrderValidationError):
        Order("NotACustomer", coffee, 3.5)

def test_coffee_must_be_coffee_object():
    customer = Customer("Jake")
    with pytest.raises(OrderValidationError):
        Order(customer, "NotACoffee", 4.0)

def test_price_must_be_number():
    customer = Customer("Nia")
    coffee = Coffee("Flat White")
    with pytest.raises(OrderValidationError):
        Order(customer, coffee, "not_a_number")

def test_price_must_be_in_range():
    customer = Customer("Leo")
    coffee = Coffee("Macchiato")

    with pytest.raises(OrderValidationError):
        Order(customer, coffee, 0.5)  # Below 1.0

    with pytest.raises(OrderValidationError):
        Order(customer, coffee, 10.5)  # Above 10.0

def test_price_rounds_to_two_decimals():
    customer = Customer("Eve")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 4.567)
    assert order.price == 4.57

def test_str_representation():
    customer = Customer("Zoe")
    coffee = Coffee("Americano")
    order = Order(customer, coffee, 2.0)
    assert str(order) == "Zoe has ordered: Americano at £2.00"

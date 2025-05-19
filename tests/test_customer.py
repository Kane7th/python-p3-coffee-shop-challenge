import pytest
from modals.customer import Customer
from modals.coffee import Coffee
from modals.order import Order
from modals.exceptions import CustomerValidationError

def setup_function():
    # Reset global orders list before each test
    Order.all_orders = []

def test_valid_customer_creation():
    customer = Customer("John")
    assert isinstance(customer, Customer)
    assert customer.name == "John"

def test_customer_name_must_be_string():
    with pytest.raises(CustomerValidationError):
        Customer(123)

def test_customer_name_cannot_be_empty():
    with pytest.raises(CustomerValidationError):
        Customer("")

def test_customer_name_cannot_be_whitespace():
    with pytest.raises(CustomerValidationError):
        Customer("   ")

def test_customer_name_length_limit():
    with pytest.raises(CustomerValidationError):
        Customer("A" * 16)  # Exceeds 15 characters

def test_customer_orders_and_coffees():
    customer = Customer("Jane")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    Order(customer, coffee1, 4.0)
    Order(customer, coffee2, 5.0)
    Order(customer, coffee1, 3.5)

    orders = customer.orders()
    assert len(orders) == 3
    assert set(customer.coffees()) == {coffee1, coffee2}

def test_create_order():
    customer = Customer("Alex")
    coffee = Coffee("Mocha")
    order = customer.create_order(coffee, 5.5)

    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.5

def test_most_aficionado_single_top_spender():
    coffee = Coffee("Cappuccino")
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    Order(c1, coffee, 4.0)
    Order(c1, coffee, 5.0)
    Order(c2, coffee, 6.0)

    result = Customer.most_aficionado(coffee)
    assert result == [c1]  # Alice spent 9.0, Bob spent 6.0

def test_most_aficionado_tie():
    coffee = Coffee("Flat White")
    c1 = Customer("Ella")
    c2 = Customer("Mia")
    Order(c1, coffee, 5.0)
    Order(c2, coffee, 5.0)

    result = Customer.most_aficionado(coffee)
    assert set(result) == {c1, c2}

def test_most_aficionado_no_orders():
    coffee = Coffee("Macchiato")
    result = Customer.most_aficionado(coffee)
    assert result is None

def test_str_representation():
    customer = Customer("Neo")
    assert str(customer) == "\nThe next Customer is: Neo"

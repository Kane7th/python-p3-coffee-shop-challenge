import pytest
from modals.coffee import Coffee
from modals.customer import Customer
from modals.order import Order
from modals.exceptions import CoffeeValidationError

def setup_function():
    # Clear all_orders list before each test
    Order.all_orders = []

def test_valid_coffee_creation():
    coffee = Coffee("Latte")
    assert isinstance(coffee, Coffee)
    assert coffee.name == "Latte"

def test_coffee_name_must_be_string():
    with pytest.raises(CoffeeValidationError):
        Coffee(123)

def test_coffee_name_cannot_be_empty():
    with pytest.raises(CoffeeValidationError):
        Coffee("")

def test_coffee_name_cannot_be_whitespace():
    with pytest.raises(CoffeeValidationError):
        Coffee("   ")

def test_coffee_name_must_be_at_least_3_chars():
    with pytest.raises(CoffeeValidationError):
        Coffee("Al")

def test_orders_and_customers_tracking():
    coffee = Coffee("Espresso")
    cust1 = Customer("Jane")
    cust2 = Customer("John")
    Order(cust1, coffee, 4.0)
    Order(cust2, coffee, 5.0)
    Order(cust1, coffee, 4.5)

    assert len(coffee.orders()) == 3
    assert set(coffee.customers()) == {cust1, cust2}
    assert coffee.num_orders() == 3
    assert coffee.average_price() == pytest.approx((4.0 + 5.0 + 4.5) / 3)

def test_average_price_zero_when_no_orders():
    coffee = Coffee("Americano")
    assert coffee.average_price() == 0.0

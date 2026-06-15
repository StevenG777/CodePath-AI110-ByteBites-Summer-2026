"""Tests for the ByteBites models.

Covers the key system behaviors:
  - order totals
  - empty totals
  - filtering menu items by category

Run with `pytest test_bytebites.py` or `python3 test_bytebites.py`.
"""

from models import Customer_Info, Mechandise_Info, Order_Info, Transaction_Info


def test_order_total():
    # A transaction's total is the sum of its selected items' prices.
    burger = Mechandise_Info("Spicy Burger", 8.99, "Mains", 4.7)
    soda = Mechandise_Info("Large Soda", 2.50, "Drinks", 4.1)
    txn = Transaction_Info([burger, soda])
    assert txn.compute_total() == 11.49


def test_empty_total():
    # A transaction with no items totals zero.
    txn = Transaction_Info()
    assert txn.compute_total() == 0


def test_filter_by_category():
    # filter_by_category returns only items in the requested category.
    burger = Mechandise_Info("Spicy Burger", 8.99, "Mains", 4.7)
    soda = Mechandise_Info("Large Soda", 2.50, "Drinks", 4.1)
    tea = Mechandise_Info("Iced Tea", 3.00, "Drinks", 4.0)
    catalog = Order_Info([burger, soda, tea])

    drinks = catalog.filter_by_category("Drinks")
    assert len(drinks) == 2
    assert {item.name for item in drinks} == {"Large Soda", "Iced Tea"}

    # A category with no matching items returns an empty list.
    assert catalog.filter_by_category("Desserts") == []


def test_add_item_updates_total():
    # Adding an item to a transaction increases the computed total.
    soda = Mechandise_Info("Large Soda", 2.50, "Drinks", 4.1)
    txn = Transaction_Info()
    assert txn.compute_total() == 0
    txn.add_item(soda)
    assert txn.compute_total() == 2.50


def test_customer_verification():
    # A customer is verified only once they have a purchase on record.
    customer = Customer_Info("Bob")
    assert customer.is_verified_user() is False
    customer.add_purchase(Transaction_Info())
    assert customer.is_verified_user() is True


if __name__ == "__main__":
    # Allow running directly without pytest.
    tests = [
        test_order_total,
        test_empty_total,
        test_filter_by_category,
        test_add_item_updates_total,
        test_customer_verification,
    ]
    for test in tests:
        test()
        print(f"PASS: {test.__name__}")
    print(f"\nAll {len(tests)} tests passed.")

"""ByteBites data models.

The four design classes from bytebites_design.md.
Attributes and methods mirror the UML diagram.
"""


class Customer_Info:
    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def __repr__(self):
        return f"Customer_Info(name={self.name!r}, purchase_history={self.purchase_history!r})"

    def is_verified_user(self):
        # A real user has at least one past purchase on record.
        return len(self.purchase_history) > 0

    def add_purchase(self, transaction):
        # Record a completed transaction in the customer's history.
        self.purchase_history.append(transaction)


class Mechandise_Info:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self):
        return (
            f"Mechandise_Info(name={self.name!r}, price={self.price!r}, "
            f"category={self.category!r}, popularity_rating={self.popularity_rating!r})"
        )

    def get_price(self):
        # Return this item's price.
        return self.price


class Order_Info:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def __repr__(self):
        return f"Order_Info(items={self.items!r})"

    def add_item(self, item):
        # Add a merchandise item to the catalog.
        self.items.append(item)

    def filter_by_category(self, category):
        # Return all catalog items belonging to the given category (e.g. "Drinks").
        return [item for item in self.items if item.category == category]

    def get_all_items(self):
        # Return the full catalog.
        return self.items


class Transaction_Info:
    def __init__(self, selected_items=None):
        self.selected_items = selected_items if selected_items is not None else []

    def __repr__(self):
        return f"Transaction_Info(selected_items={self.selected_items!r})"

    def add_item(self, item):
        # Add a selected item to this transaction.
        self.selected_items.append(item)

    def compute_total(self):
        # Sum the price of every selected item.
        return sum(item.get_price() for item in self.selected_items)

def main():
    # Sample merchandise
    burger = Mechandise_Info("Spicy Burger", 8.99, "Mains", 4.7)
    soda = Mechandise_Info("Large Soda", 2.50, "Drinks", 4.1)
    cake = Mechandise_Info("Choco Cake", 5.00, "Desserts", 4.9)

    # Catalog holding all items
    catalog = Order_Info([burger, soda, cake])

    # A transaction with a couple of selected items
    txn = Transaction_Info([burger, soda])

    # A customer with one past transaction
    customer = Customer_Info("Ada", [txn])

    def dump(label, obj):
        print(f"--- {label} ---")
        for attr, value in vars(obj).items():
            print(f"  {attr} = {value!r}")

    dump("Mechandise_Info (burger)", burger)
    dump("Mechandise_Info (soda)", soda)
    dump("Order_Info (catalog)", catalog)
    dump("Transaction_Info", txn)
    dump("Customer_Info", customer)

    print("\n=== method checks ===")
    print("burger.get_price():", burger.get_price())
    print("catalog.get_all_items() count:", len(catalog.get_all_items()))
    print("catalog.filter_by_category('Drinks'):", catalog.filter_by_category("Drinks"))
    print("txn.compute_total():", txn.compute_total(), "(expected 11.49)")

    new_customer = Customer_Info("Bob")
    print("Bob is_verified_user() before purchase:", new_customer.is_verified_user())
    new_customer.add_purchase(txn)
    print("Bob is_verified_user() after add_purchase:", new_customer.is_verified_user())

    catalog.add_item(Mechandise_Info("Iced Tea", 3.00, "Drinks", 4.0))
    print("catalog count after add_item:", len(catalog.get_all_items()))
    print("Drinks after add:", [i.name for i in catalog.filter_by_category("Drinks")])

if __name__ == "__main__":
    main()
"""ByteBites data models.

Scaffolds for the four design classes from bytebites_design.md.
Attributes mirror the UML; method bodies are left as stubs for a later step.
"""


class Customer_Info:
    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def __repr__(self):
        return f"Customer_Info(name={self.name!r}, purchase_history={self.purchase_history!r})"

    def is_verified_user(self):
        pass  # TODO

    def add_purchase(self, transaction):
        pass  # TODO


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
        pass  # TODO


class Order_Info:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def __repr__(self):
        return f"Order_Info(items={self.items!r})"

    def add_item(self, item):
        pass  # TODO

    def filter_by_category(self, category):
        pass  # TODO

    def get_all_items(self):
        pass  # TODO


class Transaction_Info:
    def __init__(self, selected_items=None):
        self.selected_items = selected_items if selected_items is not None else []

    def __repr__(self):
        return f"Transaction_Info(selected_items={self.selected_items!r})"

    def add_item(self, item):
        pass  # TODO

    def compute_total(self):
        pass  # TODO

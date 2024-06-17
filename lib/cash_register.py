#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = 0.0
        self.last_items = []

    def add_item(self, title, price, quantity=1):
        self.last_transaction = price * quantity
        self.last_items = [(title, price) for _ in range(quantity)]
        self.items.extend(self.last_items)
        self.total += self.last_transaction

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")

    def remove_item(self, title, price):
        item = (title, price)
        if item in self.items:
            self.items.remove(item)
            self.total -= price
        else:
            print(f"Item '{title}' with price {price} is not in the register.")

    def get_items(self):
        return [item[0] for item in self.items]

    def void_last_transaction(self):
        self.total -= self.last_transaction
        for item in self.last_items:
            self.items.remove(item)
        self.last_transaction = 0.0
        self.last_items = []

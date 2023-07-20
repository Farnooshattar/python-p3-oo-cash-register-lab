#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):

        self.last_price = price
        self.last_title = title
        self.last_quantity = quantity
        self.total += price * quantity

        for i in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if (self.discount == 0):
            print("There is no discount to apply.")
        else:
            # self.total_discounted = self.total-(self.total * self.discount)/100
            self.total = self.total-(self.total * self.discount)/100
            # print(
            #     f"After the discount, the total comes to ${int(self.total_discounted)}.")
            print(
                f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.total = self.total - (self.last_price * self.last_quantity)
        print(self.total)


checkout = CashRegister(20)
# checkout.add_item("apple", 3, 10)
# checkout.add_item("tomato", 2, 50)
checkout.add_item("mac", 1000, 1)
checkout.apply_discount()
checkout.void_last_transaction()

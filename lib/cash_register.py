#!/usr/bin/env python3

class CashRegister:


  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.prices = []
    self.quantities = []

  def add_item(self, title, price, quantity=1):
    self.total += (price * quantity)
    self.prices.append(price)
    self.quantities.append(quantity)
    self.items.extend([title] * quantity)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      discount_percent = self.discount/100
      self.total = (self.total - (self.total * discount_percent))
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= (self.prices[-1] * self.quantities[-1])
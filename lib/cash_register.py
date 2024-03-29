#!/usr/bin/env python3

class CashRegister:
  def __init__(self):
        self.items = {}  # Store items and their prices
        self.total = 0   # Total cost of items
        
  def add_item(self, item, price):
        """
        Add an item to the register.
        """
        if item in self.items:
            self.items[item] += price
        else:
            self.items[item] = price
        self.total += price
    
  def calculate_total(self):
        """
        Calculate the total cost of items.
        """
        return self.total
    
  def process_payment(self, amount_paid):
        """
        Process payment and return change.
        """
        if amount_paid < self.total:
            return "Insufficient payment."
        else:
            change = amount_paid - self.total
            self.total = 0  # Reset total
            self.items = {}  # Clear items
            return f"Change: {change}"

# Example usage:
register = CashRegister()

# Adding items
register.add_item("Apple", 0.75)
register.add_item("Banana", 1.00)
register.add_item("Orange", 0.50)

# Calculating total
total_cost = register.calculate_total()

# Processing payment
amount_paid = 5.00
change = register.process_payment(amount_paid)
print(change) 
pass

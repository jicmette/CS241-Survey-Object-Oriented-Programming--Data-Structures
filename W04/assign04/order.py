
from product import Product

class Order:

    def __init__(self):
        self.id = ""
        self.products = []

    def get_subtotal(self):
        total = 0
        for p in self.products:
            total += p.get_total_price()
        return total 

    def get_tax(self):
        tax = self.get_subtotal() * 0.065
        return tax

    def get_total(self):
        tot_tax = self.get_subtotal() + self.get_tax()
        return tot_tax

    def add_product(self, product):
        self.products.append(product)

    def display_receipt(self):
        print("Order: {}". format(self.id))
        for p in self.products:
            p.display()
        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))

    
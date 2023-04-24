from product import Product
from order import Order

class Customer: 

    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        order_count = len(self.orders)
        return order_count

    def get_total(self):
        total = 0
        for o in self.orders:
            total += o.get_total()
        return total

    def add_order(self, order):
        self.orders.append(order)

    def display_summary(self):
        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${:.2f}".format(self.get_total()))
    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        for o in self.orders:
            print()
            o.display_receipt() 




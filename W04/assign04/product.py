class Product:

    def __init__(self, id='', name = '', price = 0, quantity = 0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        total_price = self.price * self.quantity
        return total_price
        
    def display(self):
        self.get_total_price()
        print("{} ({}) - ${:.2f}".format(self.name, self.quantity, self.get_total_price()))


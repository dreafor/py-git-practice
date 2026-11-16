class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def get_final_price(self):
        discount_amount = self.price * self.discount / 100
        return self.price - discount_amount
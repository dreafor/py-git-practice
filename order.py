class Order:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity=1):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)

    def get_total(self):
        return sum(
            product["price"] * product["quantity"]
            for product in self.products
        )

    def show_products(self):
        for product in self.products:
            print(
                f'{product["name"]}: '
                f'{product["quantity"]} шт. '
                f'по {product["price"]} руб.'
            )


if __name__ == "__main__":
    order = Order()

    order.add_product("Ноутбук", 50000, 1)
    order.add_product("Мышь", 1500, 2)
    order.add_product("Клавиатура", 3000, 1)

    order.show_products()
    print("Общая стоимость:", order.get_total(), "руб.")
def calculate_discount(price, discount):
    return price * discount


def final_price(price, discount):
    return price - calculate_discount(price, discount)
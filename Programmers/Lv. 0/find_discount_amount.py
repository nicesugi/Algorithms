def solution1(price: int) -> int:
    if price >= 500000:
        discounted_price = price * 0.8
    elif 500000 > price >= 300000:
        discounted_price = price * 0.9
    elif 300000 > price >= 100000:
        discounted_price = price * 0.95
    else:
        discounted_price = price

    return int(discounted_price)


def solution2(price: int) -> int:
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:

            return int(price * discount_rate)

def solution(price: int) -> int:
    if price >= 500000:
        discounted_price = price * 0.8
    elif 500000 > price >= 300000:
        discounted_price = price * 0.9
    elif 300000 > price >= 100000:
        discounted_price = price * 0.95
    else:
        discounted_price = price

    return int(discounted_price)

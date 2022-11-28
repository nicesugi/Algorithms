def solution(n: int, k: int) -> int:
    food = 12000 * n
    drink = 2000 * k
    free_drink = 2000 * (n // 10)

    return food + drink - free_drink

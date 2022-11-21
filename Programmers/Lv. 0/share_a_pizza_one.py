def solution(n: int) -> int:
    pizza = n // 7
    if (n % 7) == 0:
        pizza = pizza
    else:
        pizza = pizza + 1

    return pizza

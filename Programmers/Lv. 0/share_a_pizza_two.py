def solution(person: int) -> int:
    pizza = 1
    while (pizza * 6) % person != 0:
        pizza += 1

    return pizza

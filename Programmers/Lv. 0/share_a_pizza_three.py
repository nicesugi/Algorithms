def solution(slice: int, person: int) -> int:
    pizza = 1
    while (pizza * slice) < person:
        pizza += 1

    return pizza

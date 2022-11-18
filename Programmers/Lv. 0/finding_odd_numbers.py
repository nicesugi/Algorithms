def solution(n: int) -> list:
    list = []
    for i in range(1, n+1, 2):
        list.append(i)

    return list


def solution(n: int) -> list:
    return [i for i in range(1, n+1, 2)]


def solution(n: int) -> list:
    return list(range(1, n+1, 2))


def solution(n: int) -> list:
    return [*range(1, n+1, 2)]

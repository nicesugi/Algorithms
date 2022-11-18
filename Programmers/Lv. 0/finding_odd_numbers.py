def solution(n: int) -> list:
    list = []
    for i in range(1, n+1, 2):
        list.append(i)

    return list


# 같은 내용 짧게 줄여봄
def solution(n: int) -> list:
    return [i for i in range(1, n+1, 2)]


# 더 짧게 줄여봄
def solution(n: int) -> list:
    return list(range(1, n+1, 2))

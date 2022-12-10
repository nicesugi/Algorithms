def solution3(box: list, n: int) -> int:
    return (box[0] // n) * (box[1] // n) * (box[2] // n)


def solution2(box: list, n: int) -> int:
    answer = 1
    for i in box:
        answer *= i // n
    return answer


def solution1(box: list, n: int) -> int:
    list = []
    answer = 1
    for i in box:
        list.append(i // n)
    for j in list:
        answer = answer * j
    return answer

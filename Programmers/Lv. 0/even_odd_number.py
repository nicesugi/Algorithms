def solution1(num_list: list) -> list:
    even = []
    odd = []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return [len(even), len(odd)]


def solution2(num_list: list) -> list:
    answer = [0, 0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer


def solution3(num_list: list) -> list:
    answer = [0, 0]
    for i in num_list:
        answer[i % 2] += 1

    return answer

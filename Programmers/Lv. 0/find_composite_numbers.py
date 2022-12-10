def solution2(n: int) -> int:
    """
    >>> solution(10)
    5
    >>> solution(15)
    8
    """
    answer = 0
    for i in range(1, n + 1):
        for j in range(2, i):
            if i % j == 0:
                answer += 1
                break
    return answer


def solution1(n: int) -> int:
    """
    >>> solution(10)
    5
    >>> solution(15)
    8
    """
    nums = []
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                nums.append(i)
        if nums.count(i) >= 3:
            answer += 1
    return answer

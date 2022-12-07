def solution2(numbers: list, k: int) -> int:
    return numbers[(2*(k-1)) % len(numbers)]


def solution1(numbers: list, k: int) -> int:
    while len(numbers[0::2]) < k:
        numbers += numbers
        if len(numbers[0::2]) == k:
            break
    return numbers[0::2][k-1]

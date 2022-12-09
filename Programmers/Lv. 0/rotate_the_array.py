def solution2(numbers: list, direction: str) -> list:
    if direction == "right":
        numbers = [numbers[-1]] + numbers[:-1]
    else:
        numbers = numbers[1:] + [numbers[0]]
    return numbers


def solution1(numbers: list, direction: str) -> list:
    if direction == "right":
        answer = [numbers[1:][-1]] + numbers[0 : len(numbers) - 1]
    else:
        answer = numbers[1:-1] + [numbers[1:][-1]] + [numbers[0]]
    return answer

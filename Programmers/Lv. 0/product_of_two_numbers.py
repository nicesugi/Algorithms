def solution(num1: int, num2: int) -> int:
    return num1 * num2


# or lambda form
solution = lambda num1, num2: num1 * num2


# or magic method
solution = int.__mul__

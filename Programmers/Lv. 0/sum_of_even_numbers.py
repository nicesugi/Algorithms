def solution(n: int) -> int:
    sum_even_nums = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum_even_nums += i

    return sum_even_nums

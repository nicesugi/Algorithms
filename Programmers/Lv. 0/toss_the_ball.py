def solution(numbers: list, k: int) -> int:
    while len(numbers[0::2]) < k:
        numbers += numbers
        if len(numbers[0::2]) == k:
            break
            
    return numbers[0::2][k - 1]

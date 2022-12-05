def solution(numbers: list) -> int:
    nums = sorted(numbers)[::-1]
    answer = nums[0] * nums[1]
    return answer

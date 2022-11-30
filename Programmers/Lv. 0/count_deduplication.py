def solution1(array: list, n: int) -> int:
    answer = 0
    for i in array:
        if i == n:
            answer += 1
            
    return answer

  
# 축약
def solution1(array: list, n: int) -> int:
    return len([i for i in array if i == n])

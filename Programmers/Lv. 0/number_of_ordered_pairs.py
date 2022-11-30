def solution1(n: int) -> int:
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += 1    

    return answer
  
  
# 축약
def solution1(n: int) -> int:
    return len([i for i in range(1, n + 1) if n % i == 0])

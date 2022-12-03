from itertools import *

# 시간초과
def solution(balls: int, share: int) -> int:
    balls = "".join(map(str, ([i for i in range(1, balls + 1)])))
    answer = len(list(itertools.combinations(balls, share)))
    
    return answer

import math
def solution2(balls: int, share: int) -> int:
    return math.comb(balls, share)


# 시간초과 실패
import itertools
def solution1(balls: int, share: int) -> int:
    balls = "".join(map(str, ([i for i in range(1, balls + 1)])))
    answer = len(list(itertools.combinations(balls, share)))
    
    return answer

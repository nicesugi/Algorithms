def solution(n: int) -> int:
    answer = 0
    num = str(n)
    for i in range(len(num)):
	    answer += int(num[i])

    return answer
  
  
# 축약
def solution(n: int) -> int:
  return sum([int(num[i]) for i in range(len(num))])


# map 사용
def solution(n: int) -> int:
  return sum(list(map(int, str(n))))

# 매개변수가 같은지 바로 비교
def solution1(num1: int, num2: int) -> int:
    if (num1 == num2):
        return 1
    return -1
    
    
# 매개변수의 비교값을 bool로 판별
def solution2(num1: int, num2: int) -> int:
    if (num1 == num2) == True:
        return 1
    return -1
  
    
# bool값을 2 or 0 의 수식 작성
def solution3(num1: int, num2: int) -> int:
    answer = (num1 == num2) * 2 - 1
    return answer


# or lambda form
solution3 = lambda num1, num2: (num1 == num2) * 2 - 1

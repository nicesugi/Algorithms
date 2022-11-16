# 분모의 곱을 공통분모로 하여 계산 후 최대공약수를 이용해 약분
def solution(denum1: int, num1: int, denum2: int, num2: int) -> int:
    up = (num1 * denum2) + (num2 * denum1)
    down = num1 * num2
    for i in range(min(up, down), 0, -1):
        if (up % i == 0) and (down % i == 0):
            break
    up = up // i
    down = down // i
    answer = [up, down]
    
    return answer

import math


def solution2(n: int) -> int:
    num_max = 10
    while n < math.factorial(num_max):
        num_max -= 1
    return num_max
   

def solution1(n: int) -> int:
    factorial=[]
    for i in range(1,11):
        factorial.append(math.factorial(i))

    for j in range(len(factorial)):
        if n == factorial[j]:
            return j+1
        elif n > factorial[j] and n < factorial[j+1]:
            return j+1

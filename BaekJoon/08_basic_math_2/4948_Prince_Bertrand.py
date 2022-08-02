# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
#
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
#
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19)
# 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
#
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오

#45052KB 1412ms 497B
import math
import sys


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    prime_cnt = 0

    for i in range(n + 1, (2 * n) + 1):
        if is_prime(i):
            prime_cnt += 1

    print(prime_cnt)


    # 34348KB 220ms 264B
    SIZE = 123457 * 2
    ERATOS = [True] * (SIZE)
    ERATOS[0] = ERATOS[1] = False
    for i in range(2, SIZE):
        if ERATOS[i] == False: continue
        for j in range(i * i, SIZE, i):
            ERATOS[j] = False
    while 1:
        N = int(input())
        if N == 0: break
        print(sum(ERATOS[N + 1:2 * N + 1]))
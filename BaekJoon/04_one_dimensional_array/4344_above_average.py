# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다.
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.


# 30840KB 76ms 267byte
num = int(input())

for i in range(num):
    case = list(map(int,input().split()))

    avg = sum(case[1:])/case[0]
    count = 0

    for score in case[1:]:
        if score > avg:
            count += 1

    percent = count/case[0]*100

    print(f'{percent:.3f}%')
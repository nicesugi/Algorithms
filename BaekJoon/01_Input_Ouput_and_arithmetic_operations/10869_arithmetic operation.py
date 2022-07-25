# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.


# 30840KB 68ms 113byte
a, b = input().split()
a = int(a)
b = int(b)

print(a + b)
print(a - b)
print(a * b)
print(int(a/b))
print(a % b)

# 30840KB 80ms 105byte
a, b = input().split()
a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

# 30840KB 72ms 101byte
a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(int(a/b))
print(a % b)


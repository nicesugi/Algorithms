# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.


a = input()
A = a.upper()

cnt = [0]
result = []
for i in range(ord('A'), ord('Z')+1):
  num = A.count(chr(i))
  if num > max(cnt):
    cnt = []
    cnt.append(num)
    result = []
    result.append(i)
  elif num == max(cnt):
    result.append(i)
  else:
    pass

if len(result) > 1:
  print("?")
else:
  print(chr(result[0]))
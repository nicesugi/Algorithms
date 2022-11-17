# if문 없이 작성했지만, 원소가 2개일 경우([0.1]) 중앙값이 없는데도 나옴
def solution1(array: list) -> list:
    array.sort()
    length = len(array) // 2

    return array[length]


# or lambda form
solution1 = lambda array: sorted(array)[len(array)//2]


# array를 나눈 값이 0이 아닐경우, 0일 경우의 if문 작성
def solution2(array: list) -> list:
    array.sort()
    length = len(array)
    if (length % 2) != 0:
        answer = array[length // 2]
    else:
        answer = None

    return answer

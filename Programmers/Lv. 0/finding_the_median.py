def solution(array: list) -> list:
    array.sort()
    length = len(array)
    if (length % 2) != 0:
        answer = array[length // 2]
    else:
        answer = None

    return answer

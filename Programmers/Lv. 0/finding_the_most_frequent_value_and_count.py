def solution(array: list) -> int:
    list = [0] * (max(array) + 1)
    for i in array:
        list[i] += 1
    result = list.index(max(list))

    most_frequent_count = 0
    for a in list:
        if a == max(list):
            most_frequent_count += 1
            if most_frequent_count > 1:
                result = -1

    return result

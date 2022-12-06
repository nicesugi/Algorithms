def solution(my_string: str) -> int:
    list = []
    for i in my_string:
        if i.isdigit():
            list.append(i)
    answer = sum(map(int, list))

    return answer

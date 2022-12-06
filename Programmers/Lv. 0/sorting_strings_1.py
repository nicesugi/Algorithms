def solution(my_string: str) -> list:
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()

    return answer

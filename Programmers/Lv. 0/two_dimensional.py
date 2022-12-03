def solution(num_list: list, n: int) -> list:
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i: i + n])
        
    return answer


# 축약
def solution(num_list: list, n: int) -> list:
    return [num_list[i: i + n] for i in range(0, len(num_list), n)]

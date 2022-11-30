def solution(strlist: list) -> list:
    answer = []
    for str in strlist:
        answer.append(len(str))
    
    return answer
    
    
# 축약
def solution(strlist):
    return [len(str) for str in strlist]

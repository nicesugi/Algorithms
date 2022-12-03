def solution(rsp: str) -> str:
    answer = ""
    dic = {"2": "0", "0": "5", "5": "2"}
    for i in rsp:
        answer += dic[i]
        
    return answer
    

# 축약
def solution(rsp: str) -> str:
    return ''.join([dic[i] for i in rsp])

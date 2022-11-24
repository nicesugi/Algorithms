def solution1(string: str, letter: str) -> str:
    return string.replace(letter, "")
    

def solution2(string: str, letter: str) -> str:
    list = []
    for i in string:
        if i != letter:
            list.append(i)
    answer = "".join(list)

    return answer

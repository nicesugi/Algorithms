def solution1(string: str) -> str:
    reversed_string = "".join(reversed(string))
    
    return reversed_string


def solution2(string: str) -> str:
    reversed_string = string[::-1]
    
    return reversed_string

def solution(my_string: str) -> str:
    for i in ["a", "e", "i", "o", "u"]:
        my_string = my_string.replace(i, "")
    return my_string

def solution3(dot: list) -> int:
    x, y = dot
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4


def solution2(dot: list) -> int:
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        return 4
    else:
        if dot[1] > 0:
            return 2
        return 3


def solution1(dot: list) -> int:
    if (str(dot[0]))[0] == "-":
        if (str(dot[1]))[0] == "-":
            return 3
        else:
            return 2
    elif (str(dot[0]))[0] != "-":
        if (str(dot[1]))[0] != "-":
            return 1
        else:
            return 4

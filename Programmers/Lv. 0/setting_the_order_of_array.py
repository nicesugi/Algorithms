def solution1(emergency: list) -> list:
    reversed_emergency = sorted(emergency)[::-1]
    list = []
    for i in emergency:
        list.append(reversed_emergency.index(i) + 1)

    return list


# 축약
def solution1(emergency: list) -> list:
    return [(sorted(emergency))[::-1].index(i) + 1 for i in emergency]

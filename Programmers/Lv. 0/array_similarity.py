def solution2(s1: list, s2: list) -> int:
    return len(set(s1) & set(s2))


def solution2(s1: list, s2: list) -> int:
    return len(s1 + s2) - len(list(set(s1 + s2)))

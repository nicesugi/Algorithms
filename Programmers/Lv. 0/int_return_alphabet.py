from string import ascii_lowercase

def solution(age: int) -> str:
    # alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_list = list(ascii_lowercase)
    answer = ''.join([alphabet_list[int(i)] for i in str(age)])
    
    return answer

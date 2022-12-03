def solution2(letter: str) -> str:
    morse = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", 
		"--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", 
		"--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", 
		"...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", 
		"-.--": "y", "--..": "z",
    }
    answer = ""
    letter = letter.split()
    for i in letter:
        answer += morse[i]

    return answer


# 축약
def solution2(letter: str) -> str:
    morse = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", 
		"--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", 
		"--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", 
		"...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", 
		"-.--": "y", "--..": "z",
    }
    
    return ''.join([morse[i] for i in letter.split()])


def solution1(letter: str) -> str:
    morse = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", 
		"--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", 
		"--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", 
		"...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", 
		"-.--": "y", "--..": "z",
    }
    letter = letter.split(" ")
    answer = []
    for i in letter:
        for key, value in morse.items():
            if i == key:
                answer.append(value)
    answer = "".join(answer)

    return answer

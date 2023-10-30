def solution(s, n):
    answer = ""
    for char in list(s):
        if char.isspace():
            answer += char
        # 97 ~ 122
        elif char.islower():
            answer += chr((ord(char) - 97 + n) % 26 + 97)
        # 65 ~ 90
        else:
            answer += chr((ord(char) - 65 + n) % 26 + 65)
    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))

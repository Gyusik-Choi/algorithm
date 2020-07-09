# 푸는데 너무 오래 걸렸다.
# 그리고 효율적이지 못하다.
# 다시 풀기


def solution(s):
    answer = len(s)
    half = len(s) // 2
    for i in range(1, half + 1):
        word = ""
        length = 1
        j = 0
        while j < len(s) - i:
            idx = 0
            for k in range(j, len(s) - i, i):
                idx = k
                if s[k:k + i] == s[k + i:k + i + i]:
                    length += 1
                else:
                    if length > 1:
                        word += str(length) + s[k:k + i]
                        length = 1
                        break
                    else:
                        word += s[k:k + i]
                        break
            j = idx + i
        if length > 1:
            word += str(length) + s[j:]
        else:
            word += s[j:]
        if answer > len(word):
            answer = len(word)
    return answer


print(solution("abcabcdede"))

def solution(s):
    length = len(s)

    if length % 2 != 0:
        return s[length // 2]

    return s[length // 2 - 1] + s[length // 2]

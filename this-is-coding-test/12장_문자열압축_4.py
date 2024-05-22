def get_prev(cnt, prev):
    if cnt == 1:
        return prev

    return str(cnt) + prev


def solution(s):
    length = len(s)
    min_length = length
    half = length // 2

    for unit in range(1, half + 1):
        unit_s = ''
        prev = ''
        cnt = 1

        for i in range(0, length, unit):
            cur = s[i: i + unit]

            if cur == prev:
                cnt += 1
                continue

            unit_s += get_prev(cnt, prev)

            prev = cur
            cnt = 1

        unit_s += get_prev(cnt, prev)
        min_length = min(min_length, len(unit_s))

    return min_length


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

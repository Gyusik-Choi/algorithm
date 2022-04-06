def solution(s):
    arr_s = list(s)
    # 글자수 보다 커질 수 없음
    min_length = len(s)
    start = 1

    while start <= len(s) // 2:
        temp_str = ''
        temp_length = 1
        target = arr_s[:start]
        for i in range(start, len(s), start):
            if target == arr_s[i: i + start]:
                temp_length += 1
            else:
                if temp_length > 1:
                    temp_str += str(temp_length) + ''.join(target)
                else:
                    temp_str += ''.join(target)
                temp_length = 1
                target = arr_s[i: i + start]

        # for 문 끝나고 마지막에 남은 문자열 처리
        if temp_length > 1:
            temp_str += str(temp_length) + ''.join(target)
        else:
            temp_str += ''.join(target)

        min_length = min(min_length, len(temp_str))
        start += 1

    return min_length


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

print(solution("a"))

# 문제를 이해하는데 오래걸렸다
# 이 문제는 무조건 특정 갯수대로 잘라나가야 한다

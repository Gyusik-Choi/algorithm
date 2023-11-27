# s 의 길이가 1 이상 10000 이하다
# 예를 들어 두 글자가 반복되는 입력이 주어지고 길이가 10000 이라면
# ex> ababab...
# 재귀 호출이 약 5000번 발생한다
# 파이썬의 기본 최대 재귀호출 횟수는 1000이라
# 최대 재귀 호출 길이를 5000 으로 늘렸다
import sys
sys.setrecursionlimit(5000)


def separate(s, cnt):
    if not s:
        return cnt

    if len(s) == 1:
        return cnt + 1

    first_word_cnt = 1
    first_word = s[0]
    rest_word_cnt = 0

    for i in range(1, len(s)):
        if first_word == s[i]:
            first_word_cnt += 1
        else:
            rest_word_cnt += 1

        if first_word_cnt == rest_word_cnt:
            return separate(s[first_word_cnt + rest_word_cnt:], cnt + 1)

    return cnt + 1


def solution(s):
    return separate(s, 0)


print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
print(solution("ab" * 1000))

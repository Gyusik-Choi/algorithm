def solution(s):
    return s[(len(s) - 1) // 2: len(s) // 2 + 1]


print(solution("abcde"))
print(solution("qwer"))

# solution = lambda x: x[(len(x) - 1) // 2: len(x) // 2 + 1]
# '다른 사람의 풀이' 란에서 위와 같은 풀이를 발견해서
# 이를 참고하여 풀이했다
#
# 홀수는
# 1은 뺀 값에서 2를 나눈 몫과, 원래 값에서 2를 나눈 몫이 같다
# 짝수는
# 1은 뺀 값에서 2를 나눈 몫과, 원래 값에서 2를 나눈 몫이 다르다
# (1은 뺀 값에서 2를 나눈 몫보다 원래 값에서 2를 나눈 몫이 1이 더 크다)
#
# solution("abcde")
# "abcde" 홀수 길이 문자열이 인자인 경우
# s[2: 3] 처럼 한 글자만 슬라이싱 되고
#
# solution("qwer")
# "qwer" 짝수 길이 문자열이 인자인 경우
# s[1: 3] 처럼 두 글자가 슬라이싱 된다

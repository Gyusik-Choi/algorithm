from collections import defaultdict


def solution(s):
    answer = []

    # -1 을 기본 값으로 세팅
    dic = defaultdict(lambda: -1)

    for idx, char in enumerate(s):
        if dic[char] == -1:
            answer.append(-1)
        else:
            answer.append(idx - dic[char])
        dic[char] = idx

    return answer


print(solution("banana"))
print(solution("foobar"))

# 참고
# https://stackoverflow.com/questions/30356892/defaultdict-with-default-value-1
# https://www.daleseo.com/python-collections-defaultdict/

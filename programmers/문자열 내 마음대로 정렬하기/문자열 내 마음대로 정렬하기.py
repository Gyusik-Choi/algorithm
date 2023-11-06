from collections import defaultdict


def solution(strings, n):
    words = defaultdict(list)

    for word in sorted(strings, key=lambda x: x[n]):
        words[word[n]].append(word)

    answer = []

    for value in words.values():
        answer.extend(sorted(value))

    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
# 참고
# https://docs.python.org/ko/3/howto/sorting.html

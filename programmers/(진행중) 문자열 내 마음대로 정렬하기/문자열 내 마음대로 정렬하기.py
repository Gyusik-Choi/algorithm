from collections import defaultdict


def solution(strings, n):
    arr = []

    for idx, word in enumerate(strings):
        arr.append([word[n], idx])

    words = defaultdict(list)

    for char, idx in sorted(arr):
        words[char].append(strings[idx])

    answer = []

    for key, value in words.items():
        value.sort()
        answer.extend(value)

    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))


from collections import defaultdict


def solution(s1, s2):
    word_cnt = defaultdict(int)
    for s in s1:
        word_cnt[s] += 1
    for s in s2:
        word_cnt[s] += 1
    return len(list(filter(lambda x: x[1] == 2, word_cnt.items())))


print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))

from collections import Counter


def solution(weights):
    cnt = 0
    counter = Counter(weights)

    for w, w_cnt in counter.items():
        if w_cnt > 1:
            cnt += w_cnt * (w_cnt - 1) // 2
        if w * 2 // 3 in counter:
            cnt += counter[w * 2 // 3] * w_cnt
        if w * 2 // 4 in counter:
            cnt += counter[w * 2 // 4] * w_cnt
        if w * 3 // 4 in counter:
            cnt += counter[w * 3 // 4] * w_cnt

    return cnt
    
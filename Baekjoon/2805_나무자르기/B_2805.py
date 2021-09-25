import sys


def binary_search(start, end):
    if start > end:
        return

    mid = (start + end) // 2

    sums = 0
    for i in range(len(trees)):
        tree_length = trees[i] - mid
        if tree_length > 0:
            sums += tree_length

    if sums >= M:
        answer_candidates.append(mid)
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)


N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

answer_candidates = []
binary_search(0, max(trees))
sys.stdout.write(str(max(answer_candidates)))

# 4 5
# 1 2 3 4
# 0 1 2 3 <= 1 (6)
# 0 0 1 2 <= 2 (3)

import sys
from itertools import combinations


def binary_search(start, end, target):
    if start > end:
        return end + 1

    mid = (start + end) // 2
    if comb_sums_a[mid] <= target:
        return binary_search(mid + 1, end, target)
    else:
        return binary_search(start, mid - 1, target)


N, C = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))

# 배열을 절반으로 분할
half = N // 2
weights_a = weights[:half]
weights_b = weights[half:]

comb_sums_a = []
comb_sums_b = []

# 절반으로 분할한 배열의 조합을 각각 구해서
# 각 조합 경우의 합을 배열에 추가한다
for i in range(len(weights_a) + 1):
    combs = combinations(weights_a, i)
    for comb in combs:
        comb_sums_a.append(sum(comb))

for i in range(len(weights_b) + 1):
    combs = combinations(weights_b, i)
    for comb in combs:
        comb_sums_b.append(sum(comb))

# 두 배열 중 하나만 정렬
# 정렬한 배열은 이분 탐색으로
# 한계 무게를 빠르게 찾아내고
# 정렬하지 않은 배열은
# 순차적으로 for 문을 순회한다
comb_sums_a.sort()

ways = 0
for comb_b in comb_sums_b:
    if comb_b > C:
        continue

    target_weight = C - comb_b

    ways += binary_search(0, len(comb_sums_a) - 1, target_weight)

print(ways)

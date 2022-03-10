import sys
from itertools import combinations


def binary_search(start, end, sum_b):
    while start <= end:
        mid = (start + end) // 2

        if sums_a[mid] + sum_b > C:
            end = mid - 1
        else:
            start = mid + 1

    return end + 1


# 물건수, 최대 무게
N, C = map(int, sys.stdin.readline().split())
# 물건 무게
weights = list(map(int, sys.stdin.readline().split()))

half = N // 2
weights_a = weights[:half]
weights_b = weights[half:]

sums_a = []
sums_b = []

for i in range(len(weights_a) + 1):
    combination_a = combinations(weights_a, i)
    for c_a in combination_a:
        sums_a.append(sum(c_a))

for i in range(len(weights_b) + 1):
    combination_b = combinations(weights_b, i)
    for c_b in combination_b:
        sums_b.append(sum(c_b))

sums_a.sort()

left = 0
right = len(sums_a) - 1
ways = 0

for b in sums_b:
    if b > C:
        continue
    ways += binary_search(left, right, b)

print(ways)

# https://velog.io/@flaxinger/ALGO-Meet-In-The-Middle
# https://seongonion.tistory.com/105

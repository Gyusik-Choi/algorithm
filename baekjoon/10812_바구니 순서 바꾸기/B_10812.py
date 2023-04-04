import sys


N, M = map(int, sys.stdin.readline().split())
basket = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    i, j, k = i - 1, j - 1, k - 1

    mid = k
    cnt = j - k + 1

    while cnt > 0:
        target = basket[j]
        basket.remove(target)
        basket.insert(i, target)
        cnt -= 1

for b in basket:
    sys.stdout.write(str(b) + " ")

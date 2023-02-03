import sys


N, K = map(int, input().split())
cnt = 0
coins = [None] * N
for i in range(N - 1, -1, -1):
    num = int(sys.stdin.readline().strip())
    coins[i] = num

for i in range(len(coins)):
    if coins[i] <= K:
        cnt += K // coins[i]
        K %= coins[i]

print(cnt)

import sys


N, K = map(int, sys.stdin.readline().split())
coins = [0] * N
for i in range(N):
    coin = int(sys.stdin.readline().strip())
    coins[i] = coin

amount = 0
for i in range(N - 1, -1, -1):
    if K > 0:
        coin = coins[i]
        if coin <= K:
            amount += K // coin
            K %= coin
    else:
        break

print(amount)

N = int(input())
coins = list(map(int, input().split()))
coins.sort()

min_coin = 1
for coin in coins:
    if min_coin < coin:
        break

    min_coin += coin

print(min_coin)

# 5
# 3 2 1 1 9
# => 8

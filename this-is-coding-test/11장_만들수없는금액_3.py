N = int(input())
coins = list(map(int, input().split()))
coins.sort()

min_money = 1
for coin in coins:
    if min_money < coin:
        break

    min_money += coin

print(min_money)

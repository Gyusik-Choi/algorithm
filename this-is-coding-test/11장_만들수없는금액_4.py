N = int(input())
coins = list(map(int, input().split()))
coins.sort()

min_price = 1
for i, c in enumerate(coins):
    if min_price < c:
        break
    min_price += c

print(min_price)

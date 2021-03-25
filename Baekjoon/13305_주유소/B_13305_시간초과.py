N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

sums = 0
flag_idx = len(prices) - 2
min_idx = len(prices) - 2
min_price = prices[min_idx]
while min_idx >= 0:
    for i in range(min_idx, -1, -1):
        if min_price >= prices[i]:
            min_price = prices[i]
            min_idx = i

    for i in range(min_idx, flag_idx + 1):
        sums += distances[i] * min_price
    flag_idx = min_idx - 1
    min_idx -= 1
    min_price = prices[min_idx]

print(sums)

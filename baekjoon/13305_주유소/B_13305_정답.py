N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

sums = 0
for i in range(len(prices) - 2):
    if prices[i + 1] > prices[i]:
        prices[i + 1] = prices[i]

for i in range(len(prices) - 1):
    sums += prices[i] * distances[i]

print(sums)

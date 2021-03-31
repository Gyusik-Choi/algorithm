N = int(input())

prices = list()
for i in range(N):
    r, g, b = map(int, input().split())
    prices.append([r, g, b])

dp = [[0, 0, 0] for _ in range(N)]
dp[0][0] = prices[0][0]
dp[0][1] = prices[0][1]
dp[0][2] = prices[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + prices[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + prices[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + prices[i][2]

min_sums = dp[N - 1][0]
for i in range(1, 3):
    if min_sums > dp[N - 1][i]:
        min_sums = dp[N - 1][i]

print(min_sums)

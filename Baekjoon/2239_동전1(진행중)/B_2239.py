n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    coin = coins[i]
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]

print(dp[k])

# 3 10
# 1
# 2
# 5

# coin = 1
# dp[1] += dp[1 - 1]
# dp[2] += dp[2 - 1]
# dp[3] += dp[3 - 1]
# dp[4] += dp[4 - 1]
# dp[5] += dp[5 - 1]

# coin = 2
# dp[2] += dp[2 - 2]
# dp[3] += dp[3 - 2]
# dp[4] += dp[4 - 2]
# dp[5] += dp[5 - 2]

# coin = 5
# dp[5] += dp[5 - 5]

# https://yabmoons.tistory.com/491
# https://debuglog.tistory.com/78

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
# dp[6] += dp[6 - 1]
# dp[7] += dp[7 - 1]
# dp[8] += dp[8 - 1]
# dp[9] += dp[9 - 1]
# dp[10] += dp[10 - 1]

# coin = 2
# dp[2] += dp[2 - 2]
# dp[3] += dp[3 - 2]
# dp[4] += dp[4 - 2]
# dp[5] += dp[5 - 2]
# dp[6] += dp[6 - 2]
# dp[7] += dp[7 - 2]
# dp[8] += dp[8 - 2]
# dp[9] += dp[9 - 2]
# dp[10] += dp[10 - 2]

# coin = 5
# dp[5] += dp[5 - 5]
# dp[6] += dp[6 - 5]
# dp[7] += dp[7 - 5]
# dp[8] += dp[8 - 5]
# dp[9] += dp[9 - 5]
# dp[10] += dp[10 - 5]

# https://yabmoons.tistory.com/491
# https://debuglog.tistory.com/78

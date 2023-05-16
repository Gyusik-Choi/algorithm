n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n + 1)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
            continue

        if j == len(dp[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            continue

        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

print(max(dp[n - 1]))

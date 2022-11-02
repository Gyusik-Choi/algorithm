import sys


n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    t = triangle[i]
    t_end = len(t) - 1
    for j in range(len(t)):
        if j == 0:
            dp[i][j] = dp[i - 1][j]
        elif j == t_end:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
        dp[i][j] += triangle[i][j]

print(max(dp[n - 1]))

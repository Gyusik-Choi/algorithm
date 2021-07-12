import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(M + 1):
        for j in range(N + 1):
            if i == j or j == 0:
                dp[i][j] = 1

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    print(dp[M][N])

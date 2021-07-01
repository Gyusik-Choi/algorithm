# 풀이3
# 메모이제이션을 활용한 풀이다.
# (추가 정리 필요)!!!!!

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(K + 1):
        if j == 0:
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1

for i in range(1, N + 1):
    for j in range(1, K + 1):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

print(dp[N][K])

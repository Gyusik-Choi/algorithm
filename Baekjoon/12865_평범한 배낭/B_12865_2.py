N, K = map(int, input().split())
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append([W, V])

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = items[i - 1][0]
        value = items[i - 1][1]
        if weight <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])

# 참고
# https://gsmesie692.tistory.com/113
# https://st-lab.tistory.com/141

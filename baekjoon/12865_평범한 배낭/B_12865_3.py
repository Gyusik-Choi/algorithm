N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    for k in range(1, K + 1):
        W, V = items[n - 1]
        # 배낭에 담을 수 있는 경우
        if k >= W:
            # 동일한 무게로 이전에 담은 최대 가치
            # vs
            # 해당 물품의 무게를 뺀 무게로 이전에 담은 최대 가치 + 해당 물품의 가치
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - W] + V)
        else:
            dp[n][k] = dp[n - 1][k]

print(dp[N][K])

# 참고
# 파이썬 알고리즘 인터뷰
# https://gsmesie692.tistory.com/113

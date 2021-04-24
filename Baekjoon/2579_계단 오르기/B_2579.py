N = int(input())
points = []
dp = [0] * N
for i in range(N):
    p = int(input())
    points.append(p)

dp[0] = points[0]
if N >= 2:
    dp[1] = points[1] + points[0]

if N >= 3:
    if points[1] + points[2] > dp[0] + points[2]:
        dp[2] = points[1] + points[2]
    else:
        dp[2] = dp[0] + points[2]

    for i in range(3, N):
        dp[i] = max(dp[i - 2] + points[i], dp[i - 3] + points[i - 1] + points[i])

print(dp[N - 1])

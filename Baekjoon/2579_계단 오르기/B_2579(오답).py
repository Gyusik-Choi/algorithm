N = int(input())
points = []
dp = []
for i in range(N):
    p = int(input())
    points.append(p)
    dp.append([0, 0])

dp[0][0] = points[0]
dp[0][1] = 1
dp[1][0] = points[1] + points[0]
dp[1][1] = 2
if points[1] + dp[2][0] > dp[0][0] + dp[2][0]:
    dp[2][0] = points[1] + points[2]
    dp[2][1] = 2
    dp[1][1] = 0
else:
    dp[2][0] = dp[0][0] + points[2]
    dp[2][1] = 1

for i in range(3, N):
    if dp[i - 2][1] + 1 < 3 and dp[i - 1][1] + 1 < 3:
        if dp[i - 2][0] > dp[i - 1][0]:
            dp[i][0] = dp[i - 2][0] + points[i]
            dp[i][1] = dp[i - 2][1] + 1

            dp[i - 1][1] = 0
        else:
            dp[i][0] = dp[i - 1][0] + points[i]
            dp[i][1] = dp[i - 1][1] + 1

    else:
        if dp[i - 2][1] + 1 < 3 and dp[i - 1][1] + 1 == 3:
            dp[i][0] = dp[i - 2][0] + points[i]
            dp[i][1] = dp[i - 2][1] + 1

            dp[i - 1][1] = 0
        else:
            dp[i][0] = dp[i - 1][0] + points[i]
            dp[i][1] = dp[i - 1][1] + 1

print(dp[N - 1][0])

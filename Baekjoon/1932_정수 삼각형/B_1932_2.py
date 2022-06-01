import sys


n = int(sys.stdin.readline())
triangles = []
dp = []
for i in range(n):
    triangle = list(map(int, sys.stdin.readline().split()))
    triangles.append(triangle)
    dp_item = [0] * (i + 1)
    dp.append(dp_item)

dp[0][0] = triangles[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = triangles[i][j] + dp[i - 1][j]
        elif j == i:
            dp[i][j] = triangles[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = triangles[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

sys.stdout.write(str(max(dp[n - 1])))

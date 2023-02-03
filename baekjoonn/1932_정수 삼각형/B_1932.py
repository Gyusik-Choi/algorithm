import sys


n = int(input())
arr = []
for i in range(n):
    temp_arr = list(map(int, sys.stdin.readline().split()))
    arr.append(temp_arr)

dp = []
for i in range(1, n + 1):
    temp_dp = []
    for j in range(i):
        temp_dp.append(0)
    dp.append(temp_dp)

dp[0][0] = arr[0][0]
for i in range(1, len(dp)):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + arr[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]

max_sums = dp[n - 1][0]
for i in range(1, len(dp[n - 1])):
    if dp[n - 1][i] > max_sums:
        max_sums = dp[n - 1][i]
print(max_sums)

n = int(input())

dp = [0] * n
dp[0] = 1

idx2 = idx3 = idx5 = 0
num2, num3, num5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(num2, num3, num5)

    if dp[i] == num2:
        idx2 += 1
        num2 = dp[idx2] * 2
    if dp[i] == num3:
        idx3 += 1
        num3 = dp[idx3] * 3
    if dp[i] == num5:
        idx5 += 1
        num5 = dp[idx5] * 5

print(dp[n - 1])

# 참고
# 이것이 코딩테스트다

# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3
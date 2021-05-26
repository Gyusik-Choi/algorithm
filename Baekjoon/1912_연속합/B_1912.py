n = int(input())
numbers = list(map(int, input().split()))

max_num = -1001
dp = [0] * n
dp[0] = numbers[0]
if dp[0] > max_num:
    max_num = dp[0]

for i in range(1, len(numbers)):
    dp[i] = max(dp[i - 1] + numbers[i], numbers[i])
    if dp[i] > max_num:
        max_num = dp[i]

print(max_num)

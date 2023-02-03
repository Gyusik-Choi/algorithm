N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1
if N > 1:
    for i in range(1, N):
        max_cnt = 1
        for j in range(i - 1, -1, -1):
            if numbers[i] > numbers[j]:
                dp[i] = max(max_cnt, dp[j] + 1)
                max_cnt = dp[i]

        if max_cnt == 1:
            dp[i] = 1

print(max(dp))

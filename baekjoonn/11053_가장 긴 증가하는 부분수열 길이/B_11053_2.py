N = int(input())
numbers = list(map(int, input().split()))
dp = [1] * N
max_dp = 1
if N > 1:
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j] + 1)

        if dp[i] > max_dp:
            max_dp = dp[i]

print(max_dp)

def solution(x, y, n):
    inf = float('inf')
    dp = [inf] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == float('inf'):
            continue

        if i + n <= y:
            dp[i + n] = min(dp[i] + 1, dp[i + n])

        if i * 2 <= y:
            dp[i * 2] = min(dp[i] + 1, dp[i * 2])

        if i * 3 <= y:
            dp[i * 3] = min(dp[i] + 1, dp[i * 3])

    if dp[y] == float('inf'):
        return -1
    return dp[y]


# print(solution(10, 40, 5))
# print(solution(10, 40, 30))
# print(solution(2, 5, 4))
print(solution(1, 1000000, 1))

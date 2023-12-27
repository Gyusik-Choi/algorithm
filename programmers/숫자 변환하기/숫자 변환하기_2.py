def solution(x, y, n):
    inf = float('inf')
    dp = [inf] * (y + 1)
    dp[x] = 0

    for i in range(x + 1, y + 1):
        dp[i] = min(dp[i], dp[i - n])

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2])

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3])

        dp[i] += 1

    if dp[y] == float('inf'):
        return -1
    return dp[y]


# print(solution(10, 40, 5))
# print(solution(10, 40, 30))
# print(solution(2, 5, 4))
print(solution(1, 1000000, 1))

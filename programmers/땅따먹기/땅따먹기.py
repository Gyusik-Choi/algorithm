def get_max_value_except_self_idx(row, idx):
    max_value = 0

    for i in range(len(row)):
        if i == idx:
            continue
        max_value = max(max_value, row[i])

    return max_value


def solution(land):
    n = len(land)
    r = 4
    dp = [[0] * r for _ in range(n)]

    for i in range(r):
        dp[0][i] = land[0][i]

    for i in range(1, n):
        for j in range(r):
            dp[i][j] = get_max_value_except_self_idx(dp[i - 1], j) + land[i][j]

    return max(dp[n - 1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))

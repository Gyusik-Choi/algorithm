def get_dp(triangle):
    dp = []

    for i in range(len(triangle)):
        temp_dp = []

        for j in range(len(triangle[i])):
            temp_dp.append(0)

        dp.append(temp_dp)

    return dp


def get_answer(triangle):
    dp = get_dp(triangle)

    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(dp[len(triangle) - 1])


n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]
print(get_answer(t))

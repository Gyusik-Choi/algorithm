def get_gold(value):
    g = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            g[i][j] = value[i * m + j]

    return g


def get_max_gold_size(gold_info):
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        dp[i][0] = gold_info[i][0]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j - 1]) + gold_info[i][j]
                continue

            if i == 1:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1]) + gold_info[i][j]
                continue

            dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1]) + gold_info[i][j]

    return get_max_value(dp)


def get_max_value(lst):
    x = len(lst[0]) - 1
    max_gold_size = 0

    for i in range(n):
        max_gold_size = max(max_gold_size, lst[i][x])

    return max_gold_size


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    info = list(map(int, input().split()))
    gold = get_gold(info)
    print(get_max_gold_size(gold))

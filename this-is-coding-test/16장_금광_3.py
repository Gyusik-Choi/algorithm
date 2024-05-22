def get_max_value(dp):
    max_value = 0
    x = len(dp[0]) - 1

    for y in range(len(dp)):
        max_value = max(max_value, dp[y][x])

    return max_value


def get_answer(y, x, gold):
    dp_gold = [[0] * x for _ in range(y)]

    # 초기값 세팅
    for i in range(y):
        dp_gold[i][0] = gold[i][0]

    for j in range(1, x):
        for i in range(y):
            if i == 0:
                dp_gold[i][j] = gold[i][j] + max(dp_gold[i][j - 1], dp_gold[i + 1][j - 1])
            elif i == y - 1:
                dp_gold[i][j] = gold[i][j] + max(dp_gold[i - 1][j - 1], dp_gold[i][j - 1])
            else:
                dp_gold[i][j] = gold[i][j] + max(dp_gold[i - 1][j - 1], dp_gold[i][j - 1], dp_gold[i + 1][j - 1])

    return get_max_value(dp_gold)


def get_gold(info):
    gold = []

    for i in range(0, n * m, m):
        row = [info[i]]

        for j in range(i + 1, i + m):
            row.append(info[j])

        gold.append(row)

    return gold


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    gold_info = list(map(int, input().split()))

    g = get_gold(gold_info)

    print(get_answer(n, m, g))

# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
# => 19
# => 16
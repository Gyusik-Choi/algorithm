T = int(input())
for _ in range(T):
    gold_mine = []

    n, m = map(int, input().split())
    gold_mine_total = list(map(int, input().split()))

    for i in range(0, len(gold_mine_total), m):
        temp_gold_mine = []
        for j in range(i, i + m):
            temp_gold_mine.append(gold_mine_total[j])

        gold_mine.append(temp_gold_mine)

    dp = [[0] * m for _ in range(n)]

    # 각 행의 0번 인덱스 세팅
    for i in range(n):
        dp[i][0] = gold_mine[i][0]

    if n == 1:
        print(sum(gold_mine[0]))
        continue

    # m - 1 번 만큼 for 문
    # n번 만큼 for 문
    # 맨 위
    # 가운데
    # 맨 아래
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] += max(dp[i][j - 1], dp[i + 1][j - 1])
            elif i == n - 1:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i][j - 1])
            else:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

            dp[i][j] += gold_mine[i][j]

    answer = dp[0][m - 1]
    if n > 1:
        for k in range(1, n):
            answer = max(answer, dp[k][m - 1])

    print(answer)

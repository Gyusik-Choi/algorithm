T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    gold = [[0] * m for _ in range(n)]
    number_of_gold = list(map(int, input().split()))

    i = 0
    for _ in range(n):
        gold.append(number_of_gold[i: i + m])
        i += m

    # n 이 1인 경우 아래의
    # if k == 0 조건문의 dp[k + 1][j - 1] 이 index 를 넘어가서
    # 별도로 여기서 처리
    if n == 1:
        print(sum(gold[0]))
        continue

    dp = [[0] * m for _ in range(n)]
    for j in range(n):
        dp[j][0] = gold[j][0]

    for j in range(1, m):
        for k in range(n):
            if k == 0:
                dp[k][j] = max(dp[k][j - 1], dp[k + 1][j - 1]) + gold[k][j]
            elif k == n - 1:
                dp[k][j] = max(dp[k - 1][j - 1], dp[k][j - 1]) + gold[k][j]
            else:
                dp[k][j] = max(dp[k - 1][j - 1], dp[k][j - 1], dp[k + 1][j - 1]) + gold[k][j]

    max_dp = 0
    for j in range(n):
        max_dp = max(max_dp, dp[j][m - 1])
    print(max_dp)

# (1 <= n, m <= 20)

# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
# => 19
# => 16

# 1
# 1 3
# 1 2 3
# => 6

# 참고
# https://velog.io/@xxwb__/이것이-코딩-테스트다-다이나믹-프로그래밍-금광


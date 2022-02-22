from collections import deque
import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    routes = [[] for _ in range(N + 1)]
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        routes[u].append([v, c, d])

    INF = float('inf')
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[1][0] = 0

    deq = deque()
    # 시간, 비용, 시작노드
    deq.append([0, 0, 1])

    while deq:
        time, price, start = deq.popleft()

        if dp[start][price] < time:
            continue

        for end, cost, second in routes[start]:
            money = price + cost
            seconds = time + second

            if money > M:
                continue

            if dp[end][money] <= seconds:
                continue

            for j in range(money, M + 1):
                if dp[end][j] > seconds:
                    dp[end][j] = seconds
                else:
                    break

            deq.append([seconds, money, end])

    if dp[-1][-1] != INF:
        print(dp[-1][-1])
    else:
        print("Poor KCM")

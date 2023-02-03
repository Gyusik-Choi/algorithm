from collections import deque
import sys


def minimum_route(n, m, k):
    routes = [[] for _ in range(N + 1)]
    for _ in range(K):
        # 출발, 도착, 비용, 시간
        u, v, c, d = map(int, sys.stdin.readline().split())
        routes[u].append([v, c, d])

    INF = float('inf')
    dp = [[INF] * (m + 1) for _ in range(n + 1)]
    dp[1][0] = 0

    deq = deque()
    # 시간, 비용, 출발
    deq.append([0, 0, 1])

    while deq:
        dep_time, deq_price, deq_start = deq.popleft()

        if dp[deq_start][deq_price] < dep_time:
            continue

        for routes_end, routes_price, routes_time in routes[deq_start]:
            price = deq_price + routes_price
            time = dep_time + routes_time

            if price > M or dp[routes_end][price] <= time:
                continue

            for j in range(price, M + 1):
                if dp[routes_end][j] > time:
                    dp[routes_end][j] = time
                else:
                    break

            deq.append([time, price, routes_end])

    if dp[-1][-1] != INF:
        print(dp[-1][-1])
    else:
        print("Poor KCM")


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    minimum_route(N, M, K)

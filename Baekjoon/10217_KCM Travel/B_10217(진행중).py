import heapq
import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    # M 비용 이하면서 최단 시간(d)
    N, M, K = map(int, sys.stdin.readline().split())
    routes = {i: [] for i in range(1, N + 1)}
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        routes[u].append([v, c, d])

    INF = float('inf')
    dp = [[INF] * (N + 1) for _ in range(N + 1)]

    heap = []
    heapq.heappush(heap, (1, 0))


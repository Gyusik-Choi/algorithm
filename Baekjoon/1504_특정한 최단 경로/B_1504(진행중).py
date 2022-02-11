import heapq
import sys


def dijkstra(go):
    inf = float('inf')

    selected = [False] * (N + 1)
    distances = [inf] * (N + 1)

    distances[go] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        val, start = heapq.heappop(heap)

        if selected[start]:
            continue

        selected[start] = True

        for end, value in edges[start]:
            if not selected[end]:
                if distances[end] > distances[start] + value:
                    distances[end] = distances[start] + value
                    heapq.heappush(heap, (distances[end], end))
    

N, E = map(int, sys.stdin.readline().split())
edges = {i: [] for i in range(N + 1)}

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())

dijkstra(1)

# v1은 1일 수 있다, N일 수는 없다
# v2는 N일 수 있다, 1일 수는 없다

# 결국 필요한 것은
# 1 -> v1 -> v2 -> N, 1 -> v2 -> v1 -> N

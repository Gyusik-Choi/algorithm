import heapq
import sys


def dijkstra(node):
    INF = float('inf')
    selected = [False] * (V + 1)
    distances = [INF] * (V + 1)

    distances[node] = 0
    heap = []
    # 거리, 시작점
    heapq.heappush(heap, (0, node))

    while heap:
        val, start = heapq.heappop(heap)

        if selected[start]:
            continue

        selected[start] = True

        for end, value in edges[start]:
            if not selected[end]:
                if distances[start] + value < distances[end]:
                    distances[end] = val + value
                    heapq.heappush(heap, (distances[end], end))

    return distances


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
edges = {i: [] for i in range(1, V + 1)}
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edges[u].append([v, w])

arr = dijkstra(K)

for i in range(1, len(arr)):
    if arr[i] != float('inf'):
        sys.stdout.write(str(arr[i]) + "\n")
    else:
        sys.stdout.write("INF" + "\n")

import heapq


def dijkstra(start):
    inf = float('inf')
    distances = [inf] * (N + 1)
    selected = [False] * (N + 1)

    distances[start] = 0
    heap = []
    # 거리, 시작정점
    heapq.heappush(heap, (0, start))

    while heap:
        heap_distance, go = heapq.heappop(heap)

        if selected[go]:
            continue

        selected[go] = True

        for end, distance in edges[go]:
            if not selected[end]:
                if distances[end] > heap_distance + distance:
                    distances[end] = heap_distance + distance
                    heapq.heappush(heap, (distances[end], end))

    return distances


N, M = map(int, input().split())
edges = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    s, e = map(int, input().split())
    edges[s].append([e, 1])
    edges[e].append([s, 1])
X, K = map(int, input().split())

# 다익스트라 2번
# 1 -> K
# K -> X

distances_1 = dijkstra(1)
distances_K = dijkstra(K)

if distances_1[K] + distances_K[X] == float('inf'):
    print(-1)
else:
    print(distances_1[K] + distances_K[X])

# 입력

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 4 2
# 1 3
# 2 4
# 3 4

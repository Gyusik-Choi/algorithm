import heapq


def count_same_most_far_and_lowest_index(distances, target_num):
    lowest_idx = len(distances) - 1
    cnt = 0
    for i in range(len(distances) - 1, -1, -1):
        if distances[i] == target_num:
            lowest_idx = i
            cnt += 1

    return [lowest_idx, cnt]


# 거리가 1로 고정이라 dfs 로 가려했으나
# 최소 거리를 우선적으로 탐색해야 해서 다익스트라 활용
def dijkstra(start, distances, visited):
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        distance, go = heapq.heappop(heap)

        if visited[go]:
            continue

        for end in maps[go]:
            if not visited[end]:
                if distances[end] > distances[go] + 1:
                    distances[end] = distances[go] + 1
                    heapq.heappush(heap, [distances[end], end])

    return distances


N, M = map(int, input().split())
maps = {i: [] for i in range(N)}
for _ in range(M):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    maps[A].append(B)
    maps[B].append(A)

INF = float('inf')
dist = [INF] * N
dist[0] = 0
visit = [False] * N
answer = dijkstra(0, dist, visit)

most_far = max(answer)
idx, counts = count_same_most_far_and_lowest_index(answer, most_far)
print(idx + 1, most_far, counts)

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
# => 4 2 3


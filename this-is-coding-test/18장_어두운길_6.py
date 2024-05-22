import heapq

# 임의의 출발점을 정하고
# 정점 - 1 개의 간선으로
# 모든 정점들을 연결하는 최소 비용을 구한다
# mst prim 알고리즘 활용
def get_total_min_distance(n, roads):
    inf = float('inf')
    distance = [inf] * n
    mst = [False] * n
    heap = []

    distance[0] = 0
    heapq.heappush(heap, (0, 0))
    total_min_distance = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if mst[node]:
            continue

        mst[node] = True
        total_min_distance += dist

        for end_dist, end_node in roads[node]:
            if mst[end_node]:
                continue

            if distance[end_node] <= end_dist:
                continue

            distance[end_node] = end_dist
            heapq.heappush(heap, (distance[end_node], end_node))

    return total_min_distance


N, M = map(int, input().split())
total_distance = 0
road_info = {i: [] for i in range(N)}
for _ in range(M):
    X, Y, Z = map(int, input().split())
    total_distance += Z
    road_info[X].append([Z, Y])
    road_info[Y].append([Z, X])

min_distance = get_total_min_distance(N, road_info)
print(total_distance - min_distance)

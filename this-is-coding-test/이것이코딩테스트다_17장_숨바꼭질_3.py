import heapq


# 전체 맵은 모든 정점 연결 되어 있어서
# 최초에 설정한 inf 값인 경우는 없다
def find_answer(distance):
    max_distance = max(distance)
    max_distance_idx = distance.index(max_distance)
    max_distance_count = distance.count(max_distance)

    # 0번 요소가 헛간 번호 1에 해당 하므로 max_distance_idx + 1
    return [max_distance_idx + 1, max_distance, max_distance_count]


def dijkstra():
    inf = float('inf')
    distance = [inf] * (N + 1)
    visited = [False] * (N + 1)

    distance[1] = 0
    heap = []

    # 거리, 정점
    heapq.heappush(heap, (0, 1))

    while heap:
        start_dist, start_point = heapq.heappop(heap)

        if visited[start_point]:
            continue

        visited[start_point] = True

        for end_point, end_dist in barn[start_point]:
            if visited[end_point]:
                continue

            if distance[end_point] > distance[start_point] + end_dist:
                distance[end_point] = distance[start_point] + end_dist
                heapq.heappush(heap, (distance[end_point], end_point))

    # 0번 인덱스 값이 inf 라서 1번 인덱스 부터 탐색 하도록 slicing
    return find_answer(distance[1:])


N, M = map(int, input().split())
barn = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    A, B = map(int, input().split())
    barn[A].append([B, 1])
    barn[B].append([A, 1])

dist_num, dist, dist_cnt = dijkstra()
print(dist_num, dist, dist_cnt)

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
# => 4 2 3

# 2 1
# 1 2
# => 2 1 1

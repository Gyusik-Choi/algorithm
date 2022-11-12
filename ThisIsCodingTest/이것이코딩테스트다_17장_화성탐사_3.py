import heapq


def dijkstra():
    selected = [False] * (N * N)
    min_distance = [float('inf')] * (N * N)
    min_distance[0] = 0
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        start_dist, start_idx = heapq.heappop(heap)

        if selected[start_idx]:
            continue

        selected[start_idx] = True

        for end_dist, end_idx in distances[start_idx]:
            if not selected[end_idx] and min_distance[end_idx] > min_distance[start_idx] + end_dist:
                min_distance[end_idx] = min_distance[start_idx] + end_dist
                heapq.heappush(heap, (min_distance[end_idx], end_idx))

    return min_distance[N * N - 1]


def dfs(y, x):
    distance = []

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    for i in range(4):
        y_idx = y + y_direction[i]
        x_idx = x + x_direction[i]

        if 0 <= y_idx < N and 0 <= x_idx < N:
            # 거리, 좌표
            distance.append([mars[y_idx][x_idx], y_idx * N + x_idx])

    return distance


def get_distance_info():
    distance = {i: [] for i in range(N * N)}

    for i in range(N):
        for j in range(N):
            d = dfs(i, j)
            distance[i * N + j] += d

    return distance


T = int(input())
for _ in range(T):
    N = int(input())
    mars = [list(map(int, input().split())) for _ in range(N)]
    distances = get_distance_info()
    # 출발점 거리를 더해야 한다
    print(mars[0][0] + dijkstra())

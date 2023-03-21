import heapq


def dijkstra(adj, n, start_distance):
    inf = float('inf')
    distance = [inf] * (n * n)
    visited = [False] * (n * n)
    heap = []

    distance[0] = start_distance
    # 거리, 정점
    heapq.heappush(heap, (start_distance, 0))

    while heap:
        start_dist, start_point = heapq.heappop(heap)

        if visited[start_point]:
            continue

        visited[start_point] = True

        for end_point, end_dist in adj[start_point]:
            if not visited[end_point]:
                if distance[end_point] > distance[start_point] + end_dist:
                    distance[end_point] = distance[start_point] + end_dist
                    heapq.heappush(heap, (distance[end_point], end_point))

    return distance[n * n - 1]


def get_adj(space):
    n = len(space)
    adj = {i: [] for i in range(n * n)}

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            start = i * n + j

            for k in range(4):
                y, x = y_value[k] + i, x_value[k] + j

                if 0 > y or y >= n or 0 > x or x >= n:
                    continue

                end = y * n + x

                adj[start].append([end, space[y][x]])

    return adj


def get_answer():
    n = int(input())
    space = [list(map(int, input().split())) for _ in range(n)]
    adj = get_adj(space)
    return dijkstra(adj, n, space[0][0])


T = int(input())
for _ in range(T):
    print(get_answer())

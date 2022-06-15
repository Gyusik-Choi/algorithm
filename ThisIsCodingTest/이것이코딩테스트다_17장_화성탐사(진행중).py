import heapq


def dijkstra(go):
    selected = [False] * (N * N)
    distances = [float('inf')] * (N * N)
    distances[go] = 0

    heap = []
    heapq.heappush(heap, [go, 0])

    while heap:
        start, distance = heapq.heappop(heap)

        if selected[start]:
            continue

        selected[start] = True

        for end, value in spaces_dict[start]:
            if not selected[end]:
                if distances[end] > distances[go] + value:
                    distances[end] = distances[go] + value
                    heapq.heappush(heap, [end, distances[end]])
    print(distances)
    return distances


def get_routes():
    # i * N + j
    routes = {i * N + j: [] for i in range(N) for j in range(N)}

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                y_axis = y_direction[k] + i
                x_axis = x_direction[k] + j

                if i != y_axis or j != x_axis:
                    if 0 <= y_axis < N and 0 <= x_axis < N:
                        # routes[i * N + j].append([y_axis, x_axis, spaces[y_axis][x_axis]])
                        routes[i * N + j].append([y_axis * N + x_axis, spaces[y_axis][x_axis]])

    return routes


T = int(input())
for _ in range(T):
    N = int(input())
    spaces = [list(map(int, input().split())) for _ in range(N)]
    spaces_dict = get_routes()
    answer = dijkstra(0)
    print(min(answer))

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

# => 20
# => 19
# => 36

# 1
# 3
# 5 5 4
# 3 9 1
# 3 2 7

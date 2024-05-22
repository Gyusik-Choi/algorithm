import heapq


def dijkstra(go):
    heap = []
    heapq.heappush(heap, go)

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    while heap:
        distance, y, x = heapq.heappop(heap)

        if selected[y][x]:
            continue

        selected[y][x] = True

        for i in range(4):
            y_idx = y_direction[i] + y
            x_idx = x_direction[i] + x

            if 0 <= y_idx < N and 0 <= x_idx < N:
                if not selected[y_idx][x_idx]:
                    if distances[y_idx][x_idx] > spaces[y_idx][x_idx] + distance:
                        distances[y_idx][x_idx] = spaces[y_idx][x_idx] + distance
                        heapq.heappush(heap, (distances[y_idx][x_idx], y_idx, x_idx))


T = int(input())
for _ in range(T):
    N = int(input())
    spaces = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    distances = [[INF] * N for _ in range(N)]
    distances[0][0] = spaces[0][0]
    selected = [[False] * N for _ in range(N)]
    dijkstra([distances[0][0], 0, 0])
    print(distances[N - 1][N - 1])
import heapq


def dijkstra(n, go_idx, go_dist, space_dic):
    inf = float('inf')
    distance = [inf] * (n * n)
    visited = [False] * (n * n)

    # 출발점 비용을 0이 아닌
    # 입력시 받은 출발점 비용으로 설정한다
    distance[go_idx] = go_dist
    heap = []
    heapq.heappush(heap, (go_dist, go_idx))

    while heap:
        start_dist, start_idx = heapq.heappop(heap)

        if visited[start_idx]:
            continue

        visited[start_idx] = True

        for end_dist, end_idx in space_dic[start_idx]:
            if visited[end_idx]:
                continue

            if start_dist + end_dist >= distance[end_idx]:
                continue

            distance[end_idx] = start_dist + end_dist
            heapq.heappush(heap, (distance[end_idx], end_idx))

    return distance[n * n - 1]


def get_space_dict(space, n):
    dic = {i: [] for i in range(n * n)}

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            for k in range(4):
                y, x = y_value[k] + i, x_value[k] + j

                if 0 > y or y >= n or 0 > x or x >= n:
                    continue

                # (N * i) + j
                dic[n * i + j].append([space[y][x], n * y + x])

    return dic


T = int(input())
for _ in range(T):
    N = int(input())
    space_info = [list(map(int, input().split())) for _ in range(N)]
    space_dict = get_space_dict(space_info, N)
    print(dijkstra(N, 0, space_info[0][0], space_dict))

import heapq


def dijkstra(go):
    inf = float('inf')
    distances = [inf] * (N + 1)
    selected = [False] * (N + 1)

    distances[go] = 0
    heap = []
    heapq.heappush(heap, (0, go))

    while heap:
        distance, start = heapq.heappop(heap)

        if selected[start]:
            continue

        selected[start] = True

        for end, value in routes[start]:
            if not selected[end]:
                if distances[end] > distance + value:
                    distances[end] = distance + value
                    heapq.heappush(heap, (distances[end], end))

    return distances


N, M, C = map(int, input().split())
routes = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    X, Y, Z = map(int, input().split())
    routes[X].append([Y, Z])

min_distances_from_C = dijkstra(C)

cnt = 0
max_time = 0
for i in range(1, N + 1):
    time = min_distances_from_C[i]
    # if i != C and time != float('inf'):
    # C인 경우를 포함하게 되면 cnt 값이 1이 더 나와서 조건문으로 포함했으나
    # 저자의 경우 조건문으로 i != C를 사용하지 않고
    # 출력할때 cnt 에서 1을 빼는 방식으로 풀이했는데
    # 저자의 방법이 더 좋아서 수정
    if time != float('inf'):
        cnt += 1
        max_time = max(max_time, time)

# print(cnt, max_time)
print(cnt - 1, max_time)

# 입력
# 3 2 1
# 1 2 4
# 1 3 2
# => 2 4

# 문제의 조건을 보면 v1 = 1, v2 = N 이 가능하다
import heapq
import sys


def dijkstra(start_vertex, end_vertex):
    distance_values = [INF] * (N + 1)
    distance_values[start_vertex] = 0

    selected_vertex = [False] * (N + 1)

    heap = []
    heapq.heappush(heap, (0, start_vertex))

    while heap:
        value, start = heapq.heappop(heap)
        if selected_vertex[start]:
            continue
        selected_vertex[start] = True

        for end, value in adj[start]:
            if not selected_vertex[end]:
                if distance_values[end] > distance_values[start] + value:
                    distance_values[end] = distance_values[start] + value
                    heapq.heappush(heap, (distance_values[end], end))
    return distance_values[end_vertex]


N, E = map(int, sys.stdin.readline().split())
adj = {i: [] for i in range(1, N + 1)}
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append([b, c])
    adj[b].append([a, c])
v1, v2 = map(int, sys.stdin.readline().split())

INF = float('inf')
# 1 -> v1 -> v2 -> N
case_1_start = dijkstra(1, v1)
case_1_middle = dijkstra(v1, v2)
case_1_end = dijkstra(v2, N)
case_1_sums = case_1_start + case_1_middle + case_1_end
# 1 -> v2 -> v1 -> N
case_2_start = dijkstra(1, v2)
case_2_middle = dijkstra(v2, v1)
case_2_end = dijkstra(v1, N)
case_2_sums = case_2_start + case_2_middle + case_2_end

answer = min(case_1_sums, case_2_sums)
if answer == INF:
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str(answer))

# 반례
# 4 5
# 1 2 10
# 1 3 11
# 2 3 20
# 2 4 30
# 3 4 100
# 2 3
# 정답: 61

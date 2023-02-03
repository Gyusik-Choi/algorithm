# 문제의 조건을 보면 v1 = 1, v2 = N 이 가능하다
import heapq
import sys


def dijkstra(distance_values, selected_vertex, heap):
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
    return distance_values


N, E = map(int, sys.stdin.readline().split())
adj = {i: [] for i in range(1, N + 1)}
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append([b, c])
    adj[b].append([a, c])
v1, v2 = map(int, sys.stdin.readline().split())

INF = float('inf')

answer = 0
for i in range(3):
    distance = [INF] * (N + 1)
    selected = [False] * (N + 1)
    h = []
    if i == 0:
        distance[1] = 0
        heapq.heappush(h, (0, 1))
        d = dijkstra(distance, selected, h)
        if v1 == 1:
            if d[v2] == INF:
                answer = -1
                break
            else:
                answer += d[v2]
        else:
            if d[v1] == INF and d[v2] == INF:
                answer = -1
                break
            else:
                answer += min(d[v1], d[v2])
        print(answer)
    elif i == 1:
        distance[v1] = 0
        heapq.heappush(h, (0, v1))
        d = dijkstra(distance, selected, h)
        if d[v2] == INF:
            answer = -1
            break
        else:
            answer += d[v2]
        print(answer)
    else:
        distance[N] = 0
        heapq.heappush(h, (0, N))
        d = dijkstra(distance, selected, h)
        if v2 == N:
            if d[v1] == INF:
                answer = -1
                break
            else:
                answer += d[v1]
        else:
            if d[v1] == INF and d[v2] == INF:
                answer = - 1
                break
            else:
                answer += min(d[v1], d[v2])
        print(answer)
print(answer)

# 반례
# 4 5
# 1 2 10
# 1 3 11
# 2 3 20
# 2 4 30
# 3 4 100
# 2 3

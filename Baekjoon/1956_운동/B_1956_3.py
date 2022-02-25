import heapq
import sys


def dijkstra(start):
    inf = float('inf')
    distances = [inf] * (V + 1)
    selected = [False] * (V + 1)

    # 시작 노드의 거리 정보가 없을 수 있다
    if not roads[start]:
        return inf

    # distances[start] = 0
    # => 시작 노드를 0으로 만들면 안 된다
    # => if distances[end] > heap_distance + distance:
    # => 위의 조건을 만족하지 못하고 거리가 갱신되지 못하게 되며
    # => start 가 heapq 에 담기지도 못해서
    # => if start == heap_node:
    # => 결국 위의 조건을 찾지 못하게 된다
    heap = []
    # 거리, 정점
    for end_node, end_distance in roads[start]:
        distances[end_node] = end_distance
        heapq.heappush(heap, (distances[end_node], end_node))

    while heap:
        heap_distance, heap_node = heapq.heappop(heap)

        if start == heap_node:
            return heap_distance

        if selected[heap_node]:
            continue

        selected[heap_node] = True

        for end, distance in roads[heap_node]:
            if not selected[end]:
                if distances[end] > heap_distance + distance:
                    distances[end] = heap_distance + distance
                    heapq.heappush(heap, (distances[end], end))

    return float('inf')


V, E = map(int, sys.stdin.readline().split())
roads = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    roads[a].append([b, c])

min_cycle = float('inf')
for j in range(1, V + 1):
    min_cycle = min(min_cycle, dijkstra(j))

if min_cycle == float('inf'):
    sys.stdout.write(str(-1) + "\n")
else:
    sys.stdout.write(str(min_cycle) + "\n")

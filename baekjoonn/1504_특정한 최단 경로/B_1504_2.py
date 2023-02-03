import heapq
import sys


def dijkstra(go):
    inf = float('inf')

    selected = [False] * (N + 1)
    distances = [inf] * (N + 1)

    distances[go] = 0
    heap = []
    heapq.heappush(heap, (0, go))

    while heap:
        val, start = heapq.heappop(heap)

        if selected[start]:
            continue

        selected[start] = True

        for end, value in edges[start]:
            if not selected[end]:
                if distances[end] > distances[start] + value:
                    distances[end] = distances[start] + value
                    heapq.heappush(heap, (distances[end], end))

    return distances
    

N, E = map(int, sys.stdin.readline().split())
edges = {i: [] for i in range(N + 1)}

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())

distance_from_1 = dijkstra(1)
distance_from_v1 = dijkstra(v1)
distance_from_v2 = dijkstra(v2)

from_1_to_v1 = distance_from_1[v1]
from_1_to_v2 = distance_from_1[v2]
from_v1_to_v2 = distance_from_v1[v2]
from_v1_to_N = distance_from_v1[N]
from_v2_to_N = distance_from_v2[N]

case1 = from_1_to_v1 + from_v1_to_v2 + from_v2_to_N
case2 = from_1_to_v2 + from_v1_to_v2 + from_v1_to_N

if case1 != float('inf') and case2 != float('inf'):
    print(min(case1, case2))
else:
    print(-1)

# v1은 1일 수 있다, N일 수는 없다
# v2는 N일 수 있다, 1일 수는 없다

# 필요한 것은
# 1에서 v1 까지의 거리 (+ v1에서 v2까지의 거리 + v2에서 N 까지의 거리)
# 1에서 v2 까지의 거리 (+ v2에서 v1까지의 거리 + v1에서 N 까지의 거리)

# 다익스트라 연산 3번
# 1. 1에서 v1과 v2(1을 시작점으로 한번에 구할 수 있음)
# 2. v1에서 v2(둘 중 아무거나 시작점으로 해서 구할 수 있음)
# and
# 3(case1). v2에서 N(v1에서 v2의 시작점을 v1으로 했을 경우)
# 3(case2). v1에서 N(v2에서 v1의 시작점을 v2로 했을 경우)

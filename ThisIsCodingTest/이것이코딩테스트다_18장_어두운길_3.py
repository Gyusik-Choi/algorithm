import sys
import heapq


def mst_prim() -> int:
    street_lamp = 0
    mst = [False] * N
    distances = [float('inf')] * N
    distances[0] = 0
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        start_dist, start = heapq.heappop(heap)

        if mst[start]:
            continue

        mst[start] = True
        street_lamp += start_dist

        for end_dist, end in roads[start]:
            if not mst[end] and distances[end] > end_dist:
                distances[end] = end_dist
                heapq.heappush(heap, (distances[end], end))

    return street_lamp


N, M = map(int, sys.stdin.readline().split())
roads = {i: [] for i in range(N)}
total_street_lamp = 0
for _ in range(M):
    X, Y, Z = map(int, sys.stdin.readline().split())
    roads[X].append([Z, Y])
    roads[Y].append([Z, X])
    total_street_lamp += Z

min_street_lamp = mst_prim()
print(total_street_lamp - min_street_lamp)

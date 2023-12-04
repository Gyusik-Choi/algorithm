import sys
import heapq


def mst_prim(edges, house):
    inf = float('inf')
    visited = [False] * house
    mst = [inf] * house
    mst[0] = 0
    heap = []
    # 거리, 집
    heapq.heappush(heap, (0, 0))
    sums = 0

    while heap:
        dist, start = heapq.heappop(heap)

        if visited[start]:
            continue

        visited[start] = True
        sums += dist

        for end, distance in edges[start]:
            if visited[end]:
                continue

            if mst[end] <= distance:
                continue

            mst[end] = distance
            heapq.heappush(heap, (mst[end], end))

    return sums


while True:
    m, n = map(int, sys.stdin.readline().split())

    if not m and not n:
        break

    adj = dict()

    for i in range(m):
        adj[i] = []

    total_distance = 0

    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        total_distance += z
        adj[x].append([y, z])
        adj[y].append([x, z])

    sys.stdout.write(str(total_distance - mst_prim(adj, m)) + "\n")

# 참고
# https://www.acmicpc.net/board/view/54358

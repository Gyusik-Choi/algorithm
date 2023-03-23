import heapq
import sys


def mst_prim() -> int:
    inf = float('inf')

    total_cost = 0
    mst = [False] * (N + 1)
    cost = [inf] * (N + 1)

    heap = []
    # 0번 집 비용 0
    cost[0] = 0
    heapq.heappush(heap, (0, 0))

    while heap:
        start_cost, start_num = heapq.heappop(heap)

        if mst[start_num]:
            continue

        mst[start_num] = True
        total_cost += start_cost

        for end_num, end_cost in roads[start_num]:
            if mst[end_num]:
                continue

            if cost[end_num] > end_cost:
                cost[end_num] = end_cost
                heapq.heappush(heap, (cost[end_num], end_num))

    return total_cost


N, M = map(int, sys.stdin.readline().split())
roads = {i: [] for i in range(N + 1)}

total = 0

for _ in range(M):
    X, Y, Z = map(int, sys.stdin.readline().split())
    total += Z
    roads[X].append([Y, Z])
    roads[Y].append([X, Z])

# 전체 비용 - mst 비용
print(total - mst_prim())

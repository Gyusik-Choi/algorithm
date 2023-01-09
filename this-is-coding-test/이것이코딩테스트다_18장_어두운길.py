# MST-Prim
# 정점 중심
# 최소 출발점 정해야 한다
# 0번 부터 출발할 계획
# 모든 정점 연결 최소 비용

import heapq


def mst_prim():
    inf = float('inf')

    sums = 0
    mst = [False] * N
    p = [inf] * N
    p[0] = 0
    cnt = 0
    heap = []
    heapq.heappush(heap, (0, 0))

    while cnt < N:
        price, start = heapq.heappop(heap)

        if mst[start]:
            continue

        mst[start] = True

        for end, value in roads[start]:
            if p[end] > value and not mst[end]:
                p[end] = value
                heapq.heappush(heap, (value, end))

        sums += price
        cnt += 1

    return sums


N, M = map(int, input().split())
roads = {i: [] for i in range(N)}
roads_sums = 0
for _ in range(M):
    X, Y, Z = map(int, input().split())
    roads[X].append([Y, Z])
    roads[Y].append([X, Z])
    roads_sums += Z

mst_sums = mst_prim()
# 기존에 연결한 도로 총비용 - 최소 비용 연결한 도로 총비용
print(roads_sums - mst_sums)

# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11
# => 51

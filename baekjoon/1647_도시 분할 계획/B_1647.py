import heapq
import sys


def mst_prim():
    inf = float('inf')
    min_val = [inf] * (N + 1)
    mst = [False] * (N + 1)

    # 임의의 시작점 1
    min_val[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    answer = 0
    # 최소신장트리에서 분리하기 위한 최대 비용 정보
    max_val = 0

    while heap:
        val, start = heapq.heappop(heap)

        if mst[start]:
            continue

        mst[start] = True
        answer += val
        max_val = max(max_val, val)

        for end, value in roads[start]:
            if not mst[end]:
                if min_val[end] > value:
                    min_val[end] = value
                    heapq.heappush(heap, (min_val[end], end))

    return answer - max_val


N, M = map(int, sys.stdin.readline().split())
roads = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    h1, h2, v = map(int, sys.stdin.readline().split())
    roads[h1].append([h2, v])
    roads[h2].append([h1, v])

minimum_expense = mst_prim()
print(minimum_expense)

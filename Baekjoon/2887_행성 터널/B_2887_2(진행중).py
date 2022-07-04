# 해당 문제가 구글링에서 크루스칼 알고리즘으로 풀이한 방식이 비교적 많이 보이는데
# 프림 알고리즘으로도 풀이가 가능하다
# https://www.acmicpc.net/board/view/32626

import sys
import heapq


def mst_prim():
    mst = [False] * N

    total_min_distance = 0

    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        distance, start = heapq.heappop(heap)
        total_min_distance += distance

        if mst[start]:
            continue

        mst[start] = True

        for end, dist in planets_dict[start]:
            if not mst[end]:
                heapq.heappush(heap, (dist, end))

    return total_min_distance


N = int(sys.stdin.readline())
planets = []
for _ in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append([x, y, z])

planets_x = []
planets_y = []
planets_z = []

for idx, planet in enumerate(planets):
    planets_x.append([planet[0], idx])
    planets_y.append([planet[1], idx])
    planets_z.append([planet[2], idx])

planets_x.sort()
planets_y.sort()
planets_z.sort()

planets_dict = {i: [] for i in range(N)}

for i in range(N - 1):
    min_val = min(planets_x[i + 1][0] - planets_x[i][0], planets_y[i + 1][0] - planets_y[i][0], planets_z[i + 1][0] - planets_z[i][0])
    planets_dict[planets_x[i][1]].append([planets_x[i + 1][1], min_val])
    planets_dict[planets_y[i][1]].append([planets_y[i + 1][1], min_val])
    planets_dict[planets_z[i][1]].append([planets_z[i + 1][1], min_val])
    planets_dict[planets_x[i + 1][1]].append([planets_x[i][1], min_val])
    planets_dict[planets_y[i + 1][1]].append([planets_y[i][1], min_val])
    planets_dict[planets_z[i + 1][1]].append([planets_z[i][1], min_val])
print(planets_dict)
print(mst_prim())

# {0: [[1, 10], [1, 0], [3, 1], [1, 3]], 1: [[0, 10], [0, 0], [3, 1], [2, 10], [0, 3], [4, 5]], 2: [[3, 11], [1, 10], [3, 4], [4, 3]], 3: [[2, 11], [0, 1], [1, 1], [4, 0], [2, 4], [4, 20]], 4: [[3, 0], [2, 3], [1, 5], [3, 20]]}
# {0: [[1, 0], [1, 0], [3, 1], [1, 0]], 1: [[0, 0], [0, 0], [3, 1], [2, 1], [0, 0], [4, 3]], 2: [[3, 0], [1, 1], [3, 0], [4, 3]], 3: [[2, 0], [0, 1], [1, 1], [4, 0], [2, 0], [4, 3]], 4: [[3, 0], [2, 3], [1, 3], [3, 3]]}

# [[(0, 1), (0, 1), (1, 3), (0, 1)], [(0, 0), (0, 0), (1, 3), (4, 2), (0, 0), (1, 4)], [(3, 3), (4, 1), (3, 3), (3, 4)], [(3, 2), (1, 0), (1, 1), (0, 4), (3, 2), (0, 4)], [(0, 3), (1, 1), (3, 2), (0, 3)]]
# https://2hs-rti.tistory.com/entry/백준-2887번-행성-터널-파이썬

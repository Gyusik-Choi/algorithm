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

        # 이걸 여기서 수행해서 오답이 계속 나왔다
        # 이미 방문한 정점인지 확인이 안 된 상황에서 일단 더해버렸으니 답이 나올 수가 없었던 상황이다
        # total_min_distance += distance

        if mst[start]:
            continue

        mst[start] = True
        total_min_distance += distance

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
    planets_dict[planets_x[i][1]].append([planets_x[i + 1][1], planets_x[i + 1][0] - planets_x[i][0]])
    planets_dict[planets_x[i + 1][1]].append([planets_x[i][1], planets_x[i + 1][0] - planets_x[i][0]])

    planets_dict[planets_y[i][1]].append([planets_y[i + 1][1], planets_y[i + 1][0] - planets_y[i][0]])
    planets_dict[planets_y[i + 1][1]].append([planets_y[i][1], planets_y[i + 1][0] - planets_y[i][0]])

    planets_dict[planets_z[i][1]].append([planets_z[i + 1][1], planets_z[i + 1][0] - planets_z[i][0]])
    planets_dict[planets_z[i + 1][1]].append([planets_z[i][1], planets_z[i + 1][0] - planets_z[i][0]])

print(mst_prim())
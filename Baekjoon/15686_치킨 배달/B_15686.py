import sys


def combinations(idx, limit):
    if idx == limit:
        combs.append(temp[:])
    else:
        for k in range(len(chicken)):
            if not visited[k]:
                if not temp:
                    temp.append(k)
                    visited[k] = 1
                    combinations(idx + 1, limit)
                    temp.pop()
                    visited[k] = 0
                else:
                    if temp[-1] < k:
                        temp.append(k)
                        visited[k] = 1
                        combinations(idx + 1, limit)
                        temp.pop()
                        visited[k] = 0


N, M = map(int, sys.stdin.readline().split())
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

house = []
chicken = []

for i, v1 in enumerate(cities):
    for j, v2 in enumerate(v1):
        if v2 == 1:
            house.append([i, j])
        elif v2 == 2:
            chicken.append([i, j])

combs = []
temp = []
visited = [0] * len(chicken)
combinations(0, M)

min_distance_sums = float('inf')

# [[0, 1], [0, 2]]
for idx_comb, comb in enumerate(combs):
    # [0, 1]
    min_distance_per_house = [float('inf')] * len(house)
    for idx_c, c in enumerate(comb):
        y1, x1 = chicken[c]
        # 0
        # 하나의 치킨집 마다 모든 집들에 대한 거리가 나온다
        # 한 조합 안에서의 같은 집에 대한 거리를 비교해서 최소값만 골라서 합쳐준다
        # 그리고 이를 전체 최소합을 구하는 것과 비교해서 최소값을 선택한다
        for idx_h, h in enumerate(house):
            y2, x2 = h
            min_distance_per_house[idx_h] = min(min_distance_per_house[idx_h], abs(y1 - y2) + abs(x1 - x2))

    temp_min_distance_sums = sum(min_distance_per_house)
    min_distance_sums = min(min_distance_sums, temp_min_distance_sums)

sys.stdout.write(str(min_distance_sums))

# 반복문으로 비교를 해야하는데 집과 치킨집 중 어떻게 상위 하위에 위치시킬지가 까다로웠다

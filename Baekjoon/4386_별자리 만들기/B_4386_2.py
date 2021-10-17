import sys
import math


def union(y, x):
    py = find_set(y)
    px = find_set(x)

    if rank[py] >= rank[px]:
        p[px] = py
        if rank[py] == rank[px]:
            rank[px] += 1
    else:
        p[py] = px


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def get_distance(y, x):
    y_axis1, x_axis1 = y
    y_axis2, x_axis2 = x

    d = math.sqrt((y_axis1 - y_axis2) ** 2 + (x_axis1 - x_axis2) ** 2)
    return d


n = int(sys.stdin.readline().rstrip())
coordinates = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

# 이 문제에서는 좌표만 주어져서 좌표간의 거리 값이 없다
# [거리, 출발점, 도착점] 을 만들기 위한 작업
new_coordinates = []
for i in range(n - 1):
    for j in range(i + 1, n):
        dist = get_distance(coordinates[i], coordinates[j])
        # 정수로 인덱스화하기 위해서 i, j 를 출발점, 도착점으로 설정한다
        # 이 부분이 이 문제를 푸는 핵심이라고 생각한다
        # 정수로 인덱스화해야 mst 를 푸는데 필요한 출발점과 도착점을 구하고
        # 크루스칼 알고리즘을 활용할때 부모 배열을 초기화하면서
        # 추후 최상위 부모 요소를 찾거나 union 연산을 수행할 수 있다
        new_coordinates.append([dist, i, j])

p = [_ for _ in range(n + 1)]
sorted_new_coordinates = sorted(new_coordinates, key=lambda x: x[0])
# sorted_new_coordinates_length = len(sorted_new_coordinates)

cnt = 0
rank = [0] * (n + 1)
answer = 0
for c in sorted_new_coordinates:
    distance, y_coordinate, x_coordinate = c
    if find_set(y_coordinate) == find_set(x_coordinate):
        continue

    answer += distance
    union(y_coordinate, x_coordinate)

    # cnt += 1
    # # 최소신장트리의 간선 갯수는 (정점의 갯수 - 1) 이여야 한다
    # if cnt == sorted_new_coordinates_length - 1:
    #     break

sys.stdout.write(str(answer))

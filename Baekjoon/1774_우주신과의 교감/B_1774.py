import math
import sys


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    p[py] = px


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def get_distance(first, second) -> float:
    y1, x1 = first
    y2, x2 = second

    dist = math.sqrt(abs(y1 - y2) ** 2 + abs(x1 - x2) ** 2)
    return dist


N, M = map(int, sys.stdin.readline().split())
coordinates = []
for _ in range(N):
    y, x = map(int, sys.stdin.readline().split())
    coordinates.append([y, x])

linked_routes = []
for _ in range(M):
    route1, route2 = map(int, sys.stdin.readline().split())
    linked_routes.append([route1, route2])

new_coordinates = []
for i in range(len(coordinates) - 1):
    first_coordinate = coordinates[i]
    for j in range(i + 1, len(coordinates)):
        second_coordinate = coordinates[j]
        d = get_distance(first_coordinate, second_coordinate)
        new_coordinates.append([d, i + 1, j + 1])

new_coordinates.sort()

p = [_ for _ in range(N + 1)]
for i in range(len(linked_routes)):
    r1, r2 = linked_routes[i]
    if find_set(r1) != find_set(r2):
        union(r1, r2)

answer = 0
for i in range(len(new_coordinates)):
    distance, idx1, idx2 = new_coordinates[i]

    if find_set(idx1) == find_set(idx2):
        continue

    union(idx1, idx2)
    answer += distance


print("{:.2f}".format(answer))

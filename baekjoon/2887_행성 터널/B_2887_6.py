import sys


class DisjointSet:
    def __init__(self, n):
        self.p = [0] * n

        for idx in range(n):
            self.make_set(idx)

    def make_set(self, x):
        self.p[x] = x

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px >= py:
            self.p[px] = py
        else:
            self.p[py] = px


def get_min_price():
    disjoint_set = DisjointSet(N)
    min_price = 0
    cnt = 0

    for idx, planet in enumerate(planet_total):
        s, e, v = planet

        if disjoint_set.find_set(s) == disjoint_set.find_set(e):
            continue

        disjoint_set.union_set(s, e)
        min_price += v
        cnt += 1

        if cnt == N - 1:
            break

    return min_price


def get_min_dist(a, b):
    return min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


N = int(sys.stdin.readline())
planet_info = []

for i in range(N):
    p = list(map(int, sys.stdin.readline().split()))
    p.append(i)
    planet_info.append(p)

planet_x = sorted(planet_info, key=lambda x: x[0])
planet_y = sorted(planet_info, key=lambda x: x[1])
planet_z = sorted(planet_info, key=lambda x: x[2])

planet_total = []

for i in range(N - 1):
    planet_total.append([
        planet_x[i][3],
        planet_x[i + 1][3],
        get_min_dist(planet_x[i], planet_x[i + 1])
    ])

    planet_total.append([
        planet_y[i][3],
        planet_y[i + 1][3],
        get_min_dist(planet_y[i], planet_y[i + 1])
    ])

    planet_total.append([
        planet_z[i][3],
        planet_z[i + 1][3],
        get_min_dist(planet_z[i], planet_z[i + 1])
    ])

planet_total.sort(key=lambda x: x[2])
print(get_min_price())

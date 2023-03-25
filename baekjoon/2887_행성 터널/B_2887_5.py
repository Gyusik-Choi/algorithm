import sys


class DisjointSet:
    def __init__(self, n):
        self.p = [0] * n

        for k in range(n):
            self.make_set(k)

    def make_set(self, n):
        self.p[n] = n

    def find_set(self, a):
        if self.p[a] != a:
            self.p[a] = self.find_set(self.p[a])
        return self.p[a]

    def union_set(self, a, b):
        pa = self.find_set(a)
        pb = self.find_set(b)

        if pa > pb:
            self.p[pa] = pb
        else:
            self.p[pb] = pa


def mst_kruskal():
    disjoint_set = DisjointSet(N)

    total_cost = 0
    cnt = 0

    for adj in planets_adj:
        start, end, cost = adj

        if disjoint_set.find_set(start) == disjoint_set.find_set(end):
            continue

        disjoint_set.union_set(start, end)
        total_cost += cost
        cnt += 1

        if cnt == N - 1:
            break

    return total_cost


def get_distance(a, b):
    return min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


N = int(sys.stdin.readline())
# 좌표
coordinates = []
for i in range(N):
    x, y, z = list(map(int, sys.stdin.readline().split()))
    coordinates.append([x, y, z, i])

x = sorted(coordinates, key=lambda a: a[0])
y = sorted(coordinates, key=lambda a: a[1])
z = sorted(coordinates, key=lambda a: a[2])

# 시작점, 도착점, 비용
planets_adj = []

for i in range(N - 1):
    planets_adj.append([x[i][3], x[i + 1][3], get_distance(x[i], x[i + 1])])
    planets_adj.append([y[i][3], y[i + 1][3], get_distance(y[i], y[i + 1])])
    planets_adj.append([z[i][3], z[i + 1][3], get_distance(z[i], z[i + 1])])

planets_adj.sort(key=lambda a: a[2])

print(mst_kruskal())

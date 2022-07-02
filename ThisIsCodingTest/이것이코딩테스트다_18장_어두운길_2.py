import sys


class DisjointSet:
    def __init__(self, n):
        self.p = [0] * n

        for i in range(n):
            self.make_set(i)

    def make_set(self, x):
        self.p[x] = x

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)
        self.p[py] = px


N, M = map(int, sys.stdin.readline().split())
roads = []
sums = 0
for _ in range(M):
    X, Y, Z = map(int, sys.stdin.readline().split())
    roads.append([Z, X, Y])
    sums += Z

roads.sort(key=lambda x: x[0])
disjointSet = DisjointSet(N)

mst_sums = 0
for road in roads:
    z, x, y = road

    if disjointSet.find_set(x) == disjointSet.find_set(y):
        continue

    disjointSet.union_set(x, y)
    mst_sums += z

print(sums - mst_sums)

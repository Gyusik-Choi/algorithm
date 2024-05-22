from collections import deque
import sys


class DisjointSet:
    def __init__(self, n):
        self.p = [0] * (n + 1)

        for i in range(n + 1):
            self.make_set(i)

    def make_set(self, n):
        self.p[n] = n

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px > py:
            self.p[px] = py
        else:
            self.p[py] = px


def mst_kruskal(road_info):
    disjoint_set = DisjointSet(N)

    cnt = 0
    total_cost = 0

    for road in road_info:
        x, y, cost = road

        if disjoint_set.find_set(x) == disjoint_set.find_set(y):
            continue

        disjoint_set.union_set(x, y)
        cnt += 1
        total_cost += cost

        if cnt == N - 1:
            break

    return total_cost


N, M = map(int, sys.stdin.readline().split())
roads = []

total = 0

for _ in range(M):
    r = list(map(int, sys.stdin.readline().split()))
    roads.append(r)
    total += r[2]

roads.sort(key=lambda x: x[2])

deq_roads = deque()
deq_roads.extend(roads)

# 전체 비용 - mst 비용
print(total - mst_kruskal(deq_roads))

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

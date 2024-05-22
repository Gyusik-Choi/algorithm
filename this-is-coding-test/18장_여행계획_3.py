class DisjointSet:
    def __init__(self, n):
        self.p = [0] * n
        self.rank = [0] * n

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

        if self.rank[px] >= self.rank[py]:
            self.p[py] = px

            if self.rank[px] == self.rank[py]:
                self.rank[py] += 1
        else:
            self.p[px] = py


def is_travel_possible(n, info, spot):
    disjoint_set = DisjointSet(n)

    for i in range(n):
        for j in range(n):
            if info[i][j]:
                disjoint_set.union_set(i, j)

    for i in range(len(spot) - 1):
        a, b = spot[i], spot[i + 1]

        if disjoint_set.find_set(a) != disjoint_set.find_set(b):
            return 'NO'

    return 'YES'


N, M = map(int, input().split())
travel_info = [list(map(int, input().split())) for _ in range(N)]
travel_spot = list(map(int, input().split()))
print(is_travel_possible(N, travel_info, travel_spot))

# 참고
# https://ratsgo.github.io/data%20structure&algorithm/2017/11/12/disjointset/

class DisjointSet:
    def __init__(self, n):
        self.p = [0] * (n + 1)
        for i in range(1, n + 1):
            self.make_set(i)

    def make_set(self, x):
        self.p[x] = x

    def find_set(self, x):
        if self.p[x] == x:
            return self.p[x]

        self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        self.p[py] = px


def get_answer():
    for k in range(len(travel_nodes) - 1):
        if disjointSet.find_set(travel_nodes[k]) != disjointSet.find_set(travel_nodes[k + 1]):
            return False

    return True


N, M = map(int, input().split())
travel_map = [list(map(int, input().split())) for _ in range(N)]
travel_nodes = list(map(int, input().split()))

disjointSet = DisjointSet(N)
for i in range(N):
    for j in range(N):
        if travel_map[i][j]:
            disjointSet.union_set(i + 1, j + 1)


if get_answer():
    print('YES')
else:
    print('NO')

# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
# => YES

# 5 4
# 0 1 0 1 0
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 0 0 0 0 0
# 2 3 5 4
# => NO

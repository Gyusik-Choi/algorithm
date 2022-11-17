class DisjointSet:
    def __init__(self, n):
        self.p = [0] * n
        for k in range(n):
            self.make_set(k)

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


N, M = map(int, input().split())
disjointSet = DisjointSet(N)
travel_places = list()
for i in range(N):
    travel_place = list(map(int, input().split()))
    for j in range(N):
        if travel_place[j] == 1:
            disjointSet.union_set(i, j)

travel_plan = list(map(int, input().split()))
is_travel_possible = True
for i in range(1, M):
    x, y = travel_plan[i - 1] - 1, travel_plan[i] - 1
    px, py = disjointSet.find_set(x), disjointSet.find_set(y)
    if px != py:
        is_travel_possible = False
        break

if is_travel_possible:
    print('YES')
else:
    print('NO')

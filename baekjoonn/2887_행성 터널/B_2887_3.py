import sys


class DisjointSet:
    def __init__(self, n):
        self.p = [0] * n
        self.make_set(n)

    def make_set(self, n):
        for x in range(n):
            self.p[x] = x

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)
        self.p[py] = px


N = int(sys.stdin.readline())

x_axis = []
y_axis = []
z_axis = []

for i in range(N):
    X, Y, Z = map(int, sys.stdin.readline().split())
    x_axis.append([X, i])
    y_axis.append([Y, i])
    z_axis.append([Z, i])

x_axis.sort()
y_axis.sort()
z_axis.sort()

total_axis = []

for i in range(N - 1):
    # 비용, 출발점, 도착점
    total_axis.append([x_axis[i + 1][0] - x_axis[i][0], x_axis[i][1], x_axis[i + 1][1]])
    total_axis.append([y_axis[i + 1][0] - y_axis[i][0], y_axis[i][1], y_axis[i + 1][1]])
    total_axis.append([z_axis[i + 1][0] - z_axis[i][0], z_axis[i][1], z_axis[i + 1][1]])

total_axis.sort()
disjointSet = DisjointSet(N)
min_cost = 0
cnt = 0
for idx, tunnel in enumerate(total_axis):
    cost, start, end = tunnel

    if disjointSet.find_set(start) == disjointSet.find_set(end):
        continue

    disjointSet.union_set(start, end)
    min_cost += cost
    cnt += 1

    if cnt == N - 1:
        break

sys.stdout.write(str(min_cost))

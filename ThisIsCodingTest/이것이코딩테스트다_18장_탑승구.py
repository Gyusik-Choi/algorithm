class DisjointSet:
    def __init__(self, n):
        self.p = [0] * (n + 1)

        for i in range(1, n + 1):
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
        self.p[px] = py


G = int(input())
P = int(input())

gates = []
for _ in range(P):
    g = int(input())
    gates.append(g)

disjointSet = DisjointSet(G)
answer = 0

for gate in gates:
    g = disjointSet.find_set(gate)

    if g == 0:
        break

    disjointSet.union_set(g, g - 1)
    answer += 1

print(answer)

# 4
# 3
# 4
# 1
# 1
# => 2

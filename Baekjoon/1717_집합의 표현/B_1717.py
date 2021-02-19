class DisjointSet:
    def __init__(self, s):
        self.size = s
        self.p = [0] * (s + 1)
        for j in range(s + 1):
            self.make_set(j)

    def make_set(self, x):
        self.p[x] = x

    def find_set(self, x):
        if self.p[x] == x:
            return x
        self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)
        self.p[py] = px


n, m = map(int, input().split())

operations = []
for i in range(m):
    x, y, z = map(int, input().split())
    operations.append([x, y, z])

disjoint = DisjointSet(n)

for i in range(len(operations)):
    operation = operations[i]
    o = operation[0]
    a = operation[1]
    b = operation[2]
    if o == 0:
        disjoint.union(a, b)
    else:
        fa = disjoint.find_set(a)
        fb = disjoint.find_set(b)
        if fa == fb:
            print("YES")
        else:
            print("NO")

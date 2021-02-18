class DisjointSet:
    def __init__(self, n):
        self.size = n
        self.p = [0] * (n + 1)
        self.rank = [0] * (n + 1)
        for i in range(n + 1):
            self.make_set(i)

    def make_set(self, x):
        self.p[x] = x

    def find_set(self, x):
        if self.p[x] == x:
            return x
        self.p[x] = self.find_set(self.p[x])

    def union(self, x, y):
        px = self.find_set(self.p[x])
        py = self.find_set(self.p[y])

        if self.rank[px] > self.rank[py]:
            self.p[py] = px
        else:
            self.p[px] = py
            if self.rank[px] == self.rank[py]:
                self.rank[py] += 1

    def __str__(self):
        disjoint_p = "["
        for i in range(len(self.p)):
            disjoint_p += str(self.p[i]) + ", "
        disjoint_p = disjoint_p.rstrip(", ")
        disjoint_p += "]"
        return disjoint_p


disjoint = DisjointSet(8)
disjoint.union(1, 3)
disjoint.union(2, 3)
disjoint.union(5, 6)
disjoint.union(6, 8)
disjoint.union(1, 5)
disjoint.union(6, 7)
print(disjoint)
print(disjoint.rank)

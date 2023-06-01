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

    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        # px 가 py 보다 크거나 같을 경우
        # px 를 py 쪽으로 합친다
        if px >= py:
            self.p[px] = py
        # px 가 py 보다 작을 경우
        # py 를 px 쪽으로 합친다
        else:
            self.p[py] = px

    def __str__(self):
        disjoint_p = "["

        for i in range(len(self.p)):
            disjoint_p += str(self.p[i]) + ", "

        disjoint_p = disjoint_p.rstrip(", ")
        disjoint_p += "]"
        return disjoint_p


disjoint_set = DisjointSet(8)
disjoint_set.union(1, 3)
disjoint_set.union(2, 3)
disjoint_set.union(3, 4)
disjoint_set.union(4, 5)
disjoint_set.union(6, 8)
disjoint_set.union(6, 7)
print(disjoint_set)

# 참고
# https://www.youtube.com/watch?v=Ha0w2dJa2Nk

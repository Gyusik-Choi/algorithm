import sys


class DisjointSet:
    def __init__(self, n):
        self.p = [0] * (n + 1)
        for i in range(1, n + 1):
            self.p[i] = i

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


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
gates = [int(sys.stdin.readline()) for _ in range(P)]

answer = 0
disjointSet = DisjointSet(G)
for idx, gate in enumerate(gates):
    g = disjointSet.find_set(gate)

    if g == 0:
        break
    else:
        answer += 1
        disjointSet.union_set(g, g - 1)

sys.stdout.write(str(answer) + "\n")

# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4
#
# 처음에는 총 4개를 도킹할 수 있는데 왜 답이 3일까 의문이었다.
# 문제의 조건을 다시 보니
# "어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우 그 시점에서 공항의 운행을 중단한다"
# 라는 조건이 있다.
# 그래서 이 경우 2번째 3에서 공항의 운행을 중단하므로 3개까지 도킹이 가능하다.

class DisjointSet:
    def __init__(self, n):
        self.p = [0] * n

        for i in range(n):
            self.make_set(i)

    def make_set(self, i):
        self.p[i] = i

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        # 값이 작은 쪽을 부모로 설정
        if px >= py:
            self.p[px] = py
        else:
            self.p[py] = px


def mst_kruskal(vertex, edge):
    disjoint_set = DisjointSet(vertex)
    min_sums = 0
    cnt = 0

    for i in range(edge):
        s, e, v = routes[i]

        if disjoint_set.find_set(s) == disjoint_set.find_set(e):
            continue

        disjoint_set.union_set(s, e)
        min_sums += v
        cnt += 1

        if cnt == V - 1:
            break

    return min_sums


# 정점, 간선
V, E = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(E)]
routes.sort(key=lambda x: x[2])

print(mst_kruskal(V, E))

# 참고
# https://m.blog.naver.com/ssarang8649/221038259400


# 입력값
# 7 11
# 0 5 60
# 0 1 32
# 0 2 31
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51
# => 175

# 6 10
# 0 1 1
# 0 2 3
# 0 3 2
# 1 2 4
# 1 4 8
# 2 3 5
# 2 4 6
# 2 5 7
# 3 5 10
# 4 5 9
# => 19

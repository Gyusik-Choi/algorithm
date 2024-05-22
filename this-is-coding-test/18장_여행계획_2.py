class DisjointSet:
    def __init__(self, n):
        self.p = [0] * (n + 1)

        for k in range(n + 1):
            self.make_set(k)

    def make_set(self, num):
        self.p[num] = num

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        # self.p[py] = px
        # 위와 같은 방법도 가능 한데
        # 이번 풀이는 아래의 방법 활용
        # 값이 작은 쪽을 부모로 설정

        if py >= px:
            self.p[py] = px
        else:
            self.p[px] = py


N, M = map(int, input().split())
travel_info = [list(map(int, input().split())) for _ in range(N)]
travel_spot = list(map(int, input().split()))

disjointSet = DisjointSet(N)

for i in range(N):
    for j in range(N):
        if travel_info[i][j]:
            if disjointSet.find_set(i + 1) != disjointSet.find_set(j + 1):
                disjointSet.union_set(i + 1, j + 1)

is_travel_possible = True

for i in range(M - 1):
    if disjointSet.find_set(travel_spot[i]) != disjointSet.find_set(travel_spot[i + 1]):
        is_travel_possible = False
        break

if is_travel_possible:
    print('YES')
else:
    print('NO')

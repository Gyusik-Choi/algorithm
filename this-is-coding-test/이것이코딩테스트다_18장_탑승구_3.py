class DisjointSet:
    def __init__(self, n):
        self.p = [0] * (n + 1)

        for k in range(1, n + 1):
            self.make_set(k)

    def make_set(self, n):
        self.p[n] = n

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])

        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        self.p[py] = px


G = int(input())
P = int(input())
# 도킹 가능한 탑승구 번호
gate = [int(input()) for _ in range(P)]

disjoint_set = DisjointSet(G)

cnt = 0

for g in gate:
    # if not disjointSet.find_set(g):
    #     break
    #
    # disjointSet.union_set(g - 1, g)

    # 위의 방법은 안 된다
    # 예를 들어
    # 게이트 4개, 비행기 5대고 도킹 가능한 탑승구 번호가 4 4 4 4 1 이라고 가정해 보자
    # 위의 방법을 따라서
    # 4 4 4 4 1 을 for loop 를 하나씩 돌면서 도킹을 진행을 해본다
    # 첫 번째 4를 돌면 [0, 1, 2, 3, 3]
    # 두 번째 4를 돌면 [0, 1, 2, 3, 3]
    # 세 번째 4를 돌면 [0, 1, 2, 3, 3]
    # 네 번째 4를 돌면 [0, 1, 2, 3, 3]
    # 다섯 번째 1를 돌면 [0, 0, 2, 3, 3]
    # 4를 돌면서 disjointSet 의 p 배열이 제대로 갱신 되지 못한다
    # 4가 반복 되면서 점차 낮은 탑승구 번호에 도킹을 해야 하는데
    # 그러지 못하고 있다
    # find_set 을 수행한 값을 받아서 그 값과 그 보다 1 작은 값을 union_set 을 해줘야 하는데
    # find_set 값을 점검만 하고 같은 값을 반복 하고 있다
    # 4를 여러번 돌아도 union_set 을 계속 4와 3을 반복 하므로
    # p 배열의 3과 4에 해당 하는 값이 각각 3으로 변하지 않는다

    num = disjoint_set.find_set(g)

    if not num:
        break

    disjoint_set.union_set(num - 1, num)
    cnt += 1


print(cnt)

# 4
# 4
# 4
# 4
# 4
# 1
# => 5

# 4
# 5
# 4
# 4
# 4
# 4
# 1
# => 4

# 4
# 4
# 4
# 1
# 2
# 2
# => 3

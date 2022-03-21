def union_set(x, y):
    px = find_set(x)
    py = find_set(y)

    if height[px] >= height[py]:
        p[py] = px
        if height[px] == height[py]:
            height[py] += 1
    else:
        p[px] = py


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def make_set(x):
    p[x] = x


N, M = map(int, input().split())

p = [0] * (N + 1)
height = [0] * (N + 1)

for i in range(1, N + 1):
    make_set(i)

for _ in range(M):
    operation, student1, student2 = map(int, input().split())

    if not operation:
        union_set(student1, student2)
    else:
        if find_set(student1) == find_set(student2):
            print('YES')
        else:
            print('NO')

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

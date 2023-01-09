def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]


def union(x, y):
    # x의 대표자, y의 대표자를 찾아야 한다
    p[find_set(y)] = find_set(x)


N = 8
p = [0] * (N + 1)
for i in range(1, N + 1):
    make_set(i)

union(1, 3)
union(2, 3)
union(5, 6)
union(6, 8)
union(1, 5)
union(6, 7)
print(p)
# [0, 2, 2, 1, 4, 2, 2, 2, 5]

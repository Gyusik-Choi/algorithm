import sys


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        p[py] = px
        size[px] += size[py]


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def make_set(x):
    p[x] = x


T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())

    p = [0] * (200000 + 1)
    for i in range(200001):
        make_set(i)

    size = [1] * (200000 + 1)

    names = {}
    idx = 1
    for _ in range(F):
        name1, name2 = sys.stdin.readline().split()

        if name1 not in names:
            names[name1] = idx
            idx += 1

        if name2 not in names:
            names[name2] = idx
            idx += 1

        union(names[name1], names[name2])
        val = find_set(names[name1])
        sys.stdout.write(str(size[val]) + "\n")

import sys
sys.setrecursionlimit(10 ** 6)


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if rank[px] >= rank[py]:
        p[py] = px
        if rank[px] == rank[py]:
            rank[py] += 1
    else:
        p[px] = py


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


n, m = map(int, sys.stdin.readline().split())
p = [_ for _ in range(n + 1)]
rank = [0] * (n + 1)
flag = False
for i in range(m):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(find_set(num1), find_set(num2))
    if find_set(num1) == find_set(num2):
        sys.stdout.write(str(i + 1))
        flag = True
        break
    else:
        union(num1, num2)

if not flag:
    sys.stdout.write(str(0))

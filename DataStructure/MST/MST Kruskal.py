def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


V, E = map(int, input().split())
adj = []
for i in range(E):
    s, e, v = list(map(int, input().split()))
    adj.append([s, e, v])
adj.sort(key=lambda x: x[2])


p = [0] * V
for i in range(V):
    make_set(i)
rank = [0] * V

mst = []
cnt = 0
result = 0
while cnt < V - 1:
    for i in range(E):
        st, en, va = adj[i][0], adj[i][1], adj[i][2]
        if find_set(st) == find_set(en):
            continue
        result += va
        mst.append(adj[i])
        union(st, en)
        cnt += 1
        if cnt == V - 1:
            break


print(p)
print(rank)
print(mst)
print(result)


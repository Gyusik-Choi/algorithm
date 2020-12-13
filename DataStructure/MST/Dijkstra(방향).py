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

V, E = map(int, input().split())
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, v = map(int, input().split())
    adj[s].append([e, v])
    adj[e].append([s, v])

INF = float('inf')
key = [INF] * V
p = [-1] * V
mst = [False] * V
key[0] = 0
cnt = 0
while cnt < V:
    min_num = INF
    u = -1
    for i in range(V):
        if not mst[i] and key[i] < min_num:
            min_num = key[i]
            u = i

    mst[u] = True
    for j in adj[u]:
        end = j[0]
        value = j[1]
        if not mst[end] and key[end] > value + min_num:
            key[end] = value + min_num
            p[end] = u
    cnt += 1


print(key)
print(p)
print(mst)

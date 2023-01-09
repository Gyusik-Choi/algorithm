def dfs_recursion(go, recursion_visited):
    for vertex in road[go]:
        if vertex not in recursion_visited:
            recursion_visited.append(vertex)
            dfs_recursion(vertex, recursion_visited)
    return recursion_visited


N, M, V = map(int, input().split())
road = {i: [] for i in range(N + 1)}

for _ in range(M):
    s, e = map(int, input().split())
    road[s].append(e)
    road[e].append(s)

for node in road:
    road[node] = sorted(road[node])

visited = dfs_recursion(V, [V])
for v in visited:
    print(v, end=" ")
print()

# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

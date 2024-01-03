from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 5)


def dfs(visit, edges, start):
    cnt = 1

    def dfs_recursion(v, e, r):
        nonlocal cnt

        v[r] = cnt
        cnt += 1

        for end in e[r]:
            if not v[end]:
                dfs_recursion(v, e, end)

        return v

    return dfs_recursion(visit, edges, start)


N, M, R = map(int, sys.stdin.readline().split())
adj = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

for key in adj:
    adj[key].sort()

if not len(adj[R]):
    sys.stdout.write(str(0) + "\n")
else:
    visited = dfs([0] * (N + 1), adj, R)
    for i in range(1, N + 1):
        sys.stdout.write(str(visited[i]) + "\n")

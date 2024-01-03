from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(visited, edges, start):
    cnt = 1

    def dfs_recursion(visit, e, r):
        nonlocal cnt

        visit[r] = cnt
        cnt += 1

        for end in e[r]:
            if not visit[end]:
                dfs_recursion(visit, e, end)

        return visit

    return dfs_recursion(visited, edges, start)


N, M, R = map(int, sys.stdin.readline().split())
adj = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

for key in adj:
    adj[key].sort()

history = dfs([0] * (N + 1), adj, R)
for i in range(1, N + 1):
    sys.stdout.write(str(history[i]) + "\n")

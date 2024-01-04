from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(visited, edges, start):
    cnt = 1

    def dfs_recursion(visit, e, r):
        nonlocal cnt

        visit[r] = cnt
        cnt += 1

        for each in e[r]:
            if not visited[each]:
                dfs_recursion(visit, e, each)

        return visit
    return dfs_recursion(visited, edges, start)


N, M, R = map(int, sys.stdin.readline().split())
adj = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

for key in adj:
    adj[key].sort(reverse=True)

v = [0] * (N + 1)
history = dfs(v, adj, R)
answer = ''
for i in range(1, N + 1):
    answer += str(history[i]) + "\n"
sys.stdout.write(answer)

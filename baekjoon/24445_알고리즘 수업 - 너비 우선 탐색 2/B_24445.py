import sys
from collections import defaultdict, deque


def bfs(visited, e, r):
    cnt = 1
    visited[r] = cnt
    deq = deque([r])

    while deq:
        start = deq.popleft()

        for end in e[start]:
            if not visited[end]:
                cnt += 1
                visited[end] = cnt
                deq.append(end)

    return visited


N, M, R = map(int, sys.stdin.readline().split())
adj = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

for key in adj:
    adj[key].sort(reverse=True)

visit = bfs([0] * (N + 1), adj, R)
for i in range(1, N + 1):
    sys.stdout.write(str(visit[i]) + "\n")

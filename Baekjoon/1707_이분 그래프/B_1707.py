from collections import deque
import sys


def bfs(start):
    deq = deque()
    deq.append(start)
    visited[start] = 1
    while deq:
        go = deq.popleft()
        for node in adj[go]:
            if visited[node] == visited[go]:
                return False

            if visited[node] == 0:
                deq.append(node)
                if visited[go] == 1:
                    visited[node] = 2
                else:
                    visited[node] = 1
    return True


# 방문 안한 곳은 0/ 방문 한 곳은 1, 2로 구분
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    adj = {i: [] for i in range(1, V + 1)}
    for _ in range(E):
        s, e = map(int, sys.stdin.readline().split())
        adj[s].append(e)
        adj[e].append(s)

    flag = False
    for i in range(1, V + 1):
        if visited[i] == 0:
            if not bfs(i):
                print("NO")
                flag = True
                break
    if not flag:
        print("YES")

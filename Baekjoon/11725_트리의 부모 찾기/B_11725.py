import sys


def dfs(vertex):
    stack = [vertex]
    while stack:
        tmp = stack.pop()
        for n in node[tmp]:
            if visited[n] == 0 and n not in stack:
                stack.append(n)
                p[n] = tmp
        visited[tmp] = 1


N = int(input())
node = {i: [] for i in range(N + 1)}
for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

p = [0] * (N + 1)
visited = [0] * (N + 1)
dfs(1)

for i in range(2, N + 1):
    sys.stdout.write(str(p[i]) + '\n')

import sys


V, E = map(int, sys.stdin.readline().split())
adj = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append([b, c])


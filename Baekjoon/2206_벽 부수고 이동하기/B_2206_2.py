import sys


N, M = map(int, sys.stdin.readline().split())
maps = []
for _ in range(N):
    map = list(map(int, sys.stdin.readline().strip()))
    maps.append(map)

print(maps)

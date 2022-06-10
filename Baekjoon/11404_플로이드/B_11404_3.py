import sys


def floyd_warshall():
    for k in range(n):
        stations[k][k] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if stations[i][j] > stations[i][k] + stations[k][j]:
                    stations[i][j] = stations[i][k] + stations[k][j]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = float('inf')
stations = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if stations[a - 1][b - 1] > c:
        stations[a - 1][b - 1] = c


floyd_warshall()

for station in stations:
    for s in station:
        if s == INF:
            sys.stdout.write(str(0) + " ")
        else:
            sys.stdout.write(str(s) + " ")
    sys.stdout.write('\n')

# 참고
# https://blog.naver.com/ndb796/221234427842

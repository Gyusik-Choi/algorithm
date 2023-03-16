import sys


def print_answer():
    for i in range(n):
        for j in range(n):
            if bus[i][j] == max_cost:
                sys.stdout.write('0' + " ")
            else:
                sys.stdout.write(str(bus[i][j]) + " ")
        sys.stdout.write("\n")


def floyd_warshall():
    for i in range(n):
        bus[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                bus[i][j] = min(bus[i][k] + bus[k][j], bus[i][j])


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
max_cost = float('inf')
bus = [[max_cost] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a - 1][b - 1] = min(bus[a - 1][b - 1], c)

floyd_warshall()
print_answer()
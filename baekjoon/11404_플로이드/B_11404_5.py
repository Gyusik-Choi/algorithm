import sys


def format_answer(price):
    answer = ''

    for i, p in enumerate(price):
        for j, item in enumerate(p):
            if item == INF:
                answer += '0 '
            else:
                answer += str(item) + " "
        answer += '\n'

    return answer


def floyd_warshall(price):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                price[i][j] = min(price[i][j], price[i][k] + price[k][j])

    return format_answer(price)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = float('inf')
cost = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    cost[a - 1][b - 1] = min(cost[a - 1][b - 1], c)

for l in range(n):
    cost[l][l] = 0

sys.stdout.write(floyd_warshall(cost))

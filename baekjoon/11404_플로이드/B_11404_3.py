import sys


def print_answer():
    for i in range(n):
        for j in range(n):
            if cities[i][j] == float('inf'):
                sys.stdout.write(str(0) + " ")
            else:
                sys.stdout.write(str(cities[i][j]) + " ")
        sys.stdout.write("\n")


def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if k != i and i != j:
                    if cities[i][k] + cities[k][j] < cities[i][j]:
                        cities[i][j] = cities[i][k] + cities[k][j]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cities = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if cities[a - 1][b - 1] > c:
        cities[a - 1][b - 1] = c

floyd_warshall()
print_answer()

# https://www.acmicpc.net/board/view/100539
# 100001 로 최대값을 잡아 놓으면 안 된다
# 비용 자체는 100001 이 넘을 수 있다

# if k != i and i ! j:
# 조건을 통해 a -> b -> a 처럼
# 자신에서 다른 곳을 거쳐 다시 자신으로 오는 경우를 막거나
# 혹은
# for i in range(n):
#     cities[i][i] = 0
# 자기 자신의 거리 값을 0 으로 설정할 수 있다
#
# 만약 위의 if 조건이 없는데
# 자기 자신의 거리 값이 0 이 아니라 float('inf') 일 경우
# 예를 들어
# 0 -> 0 이 float('inf')
# 0 -> 2 가 3
# 2 -> 0 이 8 이라고 하면
# 0 -> 0 은 11 이 되므로 주의해야 한다

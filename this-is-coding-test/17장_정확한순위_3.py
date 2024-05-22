import sys


def count_student():
    cnt = 0

    for i in range(N):
        temp = 0

        for j in range(N):
            if grades[i][j] == float('inf') and grades[j][i] == float('inf'):
                temp += 1
                break

        if not temp:
            cnt += 1

    return cnt


def floyd_warshall():
    for i in range(N):
        grades[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                grades[i][j] = min(grades[i][j], grades[i][k] + grades[k][j])


N, M = map(int, sys.stdin.readline().split())
INF = float('inf')
grades = [[INF] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    grades[A - 1][B - 1] = 1

floyd_warshall()
sys.stdout.write(str(count_student()))

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
# => 1

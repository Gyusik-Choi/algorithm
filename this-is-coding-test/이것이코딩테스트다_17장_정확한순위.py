def floyd_warshall():
    for k in range(N):
        grades[k][k] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if grades[i][j] > grades[i][k] + grades[k][j]:
                    grades[i][j] = grades[i][k] + grades[k][j]


N, M = map(int, input().split())
INF = float('inf')
grades = [[INF] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    grades[A - 1][B - 1] = 1

floyd_warshall()

number_of_students = 0
for m in range(N):
    temp_number_of_students = 0

    for n in range(N):
        if m != n:
            if grades[m][n] != INF or grades[n][m] != INF:
                temp_number_of_students += 1

    if temp_number_of_students == N - 1:
        number_of_students += 1

print(number_of_students)

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
# => 1

def find_answer(g):
    answer = 0

    for i in range(N):
        is_know = True

        for j in range(N):
            if g[i][j] == INF and g[j][i] == INF:
                is_know = False
                break

        if is_know:
            answer += 1

    return answer


def floyd_warshall(g):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                grade[i][j] = min(grade[i][j], grade[i][k] + grade[k][j])

    return find_answer(g)


N, M = map(int, input().split())
INF = float('inf')
grade = [[INF] * N for _ in range(N)]

for n in range(N):
    grade[n][n] = 0

for _ in range(M):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    grade[A][B] = 1

print(floyd_warshall(grade))

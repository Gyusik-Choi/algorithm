import sys


def find_answer():
    answer = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if grades[i][j] != float('inf') or grades[j][i] != float('inf'):
                cnt += 1

        if cnt == N - 1:
            answer += 1

    return answer


def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if k != i and i != j:
                    grades[i][j] = min(grades[i][j], grades[i][k] + grades[k][j])


N, M = map(int, sys.stdin.readline().split())
grades = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    # 비용은 임의로 1로 설정
    grades[A - 1][B - 1] = 1

floyd_warshall()
print(find_answer())

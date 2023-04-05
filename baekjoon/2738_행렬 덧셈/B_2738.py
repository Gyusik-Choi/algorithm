import sys


N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# C = [[0] * N for _ in range(N)]
# 안쪽 배열의 크기는 N 이 아니라 M 으로 잡아야 한다
C = [[0] * M for _ in range(N)]

for i in range(N):
    # 안쪽 배열의 크기는 N 이 아니라 M 으로 잡아야 한다
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]

for i in range(N):
    # 안쪽 배열의 크기는 N 이 아니라 M 으로 잡아야 한다
    for j in range(M):
        sys.stdout.write(str(C[i][j]) + " ")
    sys.stdout.write("\n")

# 참고
# https://www.acmicpc.net/board/view/109953

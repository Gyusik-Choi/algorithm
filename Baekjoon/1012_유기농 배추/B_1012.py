from collections import deque
import sys


def bfs(y, x):
    deq = deque()
    deq.append([y, x])

    while deq:
        location = deq.popleft()

        y_location = location[0]
        x_location = location[1]
        visited[y_location][x_location] = 1

        for idx in range(4):
            y_idx = y_location + y_axis[idx]
            x_idx = x_location + x_axis[idx]

            if 0 <= y_idx < N and 0 <= x_idx < M:
                if field[y_idx][x_idx] == 1 and visited[y_idx][x_idx] == 0 and [y_idx, x_idx] not in deq:
                    deq.append([y_idx, x_idx])
    return


T = int(input())
for t in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())

    field = [[0] * M for _ in range(N)]
    for k in range(K):
        X, Y = map(int, sys.stdin.readline().strip().split())
        field[Y][X] = 1

    visited = [[0] * M for _ in range(N)]

    # 상 우 하 좌
    y_axis = [1, 0, -1, 0]
    x_axis = [0, 1, 0, -1]

    # 인접 숫자
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 배추가 심어져 있으면서 아직 방문하지 않은 곳
            if field[i][j] == 1 and visited[i][j] == 0:
                # 인접 숫자 1 증가
                cnt += 1
                # bfs 탐색
                bfs(i, j)
    print(cnt)

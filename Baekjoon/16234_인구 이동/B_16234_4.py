# 모든 칸을 돌면서
# 4 방향의 인접한 국경 검사
# 연합 여러개 어떻게 처리? => 하나의 bfs 사이클 안에서 처리
from collections import deque


def population_move(lock, move, average):
    for idx, m in enumerate(move):
        y, x = m
        lock[y][x] = False
        populations[y][x] = average


def bfs(visited, lock, start):
    sums = populations[start[0]][start[1]]
    cnt = 1
    move = [start]

    deq = deque()
    deq.append(start)
    visited[start[0]][start[1]] = True
    lock[start[0]][start[1]] = True

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    while deq:
        y, x = deq.popleft()

        for k in range(4):
            y_idx = y + y_value[k]
            x_idx = x + x_value[k]

            if 0 <= y_idx < N and 0 <= x_idx < N:
                if L <= abs(populations[y][x] - populations[y_idx][x_idx]) <= R:
                    if not visited[y_idx][x_idx]:
                        visited[y_idx][x_idx] = True
                        lock[y_idx][x_idx] = True
                        deq.append([y_idx, x_idx])
                        sums += populations[y_idx][x_idx]
                        cnt += 1
                        move.append([y_idx, x_idx])

    if cnt > 1:
        average = sums // cnt
        population_move(lock, move, average)
        return True

    return False


def check_move():
    answer = 0
    lock = [[False] * N for _ in range(N)]
    while True:
        visited = [[False] * N for _ in range(N)]
        move_cnt = 0

        for i, population in enumerate(populations):
            for j, p in enumerate(population):
                if not visited[i][j] and not lock[i][j]:
                    if bfs(visited, lock, [i, j]):
                        move_cnt += 1

        if not move_cnt:
            break

        answer += 1

    return answer


N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]
print(check_move())

import sys
from collections import deque


def get_avg(can_move):
    sums = 0
    number_of_people = 0

    for i, row in enumerate(can_move):
        for j, row_item in enumerate(row):
            if can_move[i][j]:
                number_of_people += 1
                sums += countries[i][j]

    if not number_of_people:
        return 0

    avg = sums // number_of_people
    return avg


def change_population(can_move):
    avg = get_avg(can_move)

    if not avg:
        return False

    for i, row in enumerate(can_move):
        for j, row_item in enumerate(row):
            if can_move[i][j]:
                countries[i][j] = avg

    return True


def bfs(start):
    deq = deque()
    deq.append(start)

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    visited = [[False] * N for _ in range(N)]
    can_move = [[False] * N for _ in range(N)]

    while deq:
        [y, x, can_move_cnt] = deq.popleft()
        visited[y][x] = True

        for idx in range(4):
            y_idx = y + y_direction[idx]
            x_idx = x + x_direction[idx]

            if 0 <= y_idx < N and 0 <= x_idx < N:
                if not visited[y_idx][x_idx]:
                    if L <= countries[y][x] - countries[y_idx][x_idx] <= R:
                        can_move_cnt += 1
                        deq.append([y_idx, x_idx, 1])

        if can_move_cnt > 0:
            can_move[y][x] = True

    change_result = change_population(can_move)

    if not change_result:
        return False

    return True


N, L, R = map(int, sys.stdin.readline().split())
countries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

days = 0
while True:
    result = bfs([0, 0, 0])
    if not result:
        break
    else:
        days += 1

print(days)

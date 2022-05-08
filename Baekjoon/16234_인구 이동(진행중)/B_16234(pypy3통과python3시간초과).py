import sys
from collections import deque


def change_population(can_move, avg):
    for can in can_move:
        y = can[0]
        x = can[1]
        countries[y][x] = avg


def bfs(start):
    deq = deque()
    deq.append(start)

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    can_move = []
    sums = 0
    number_of_people = 0

    while deq:
        [y, x] = deq.popleft()
        visited[y][x] = True
        can_move.append([y, x])
        sums += countries[y][x]
        number_of_people += 1

        for idx in range(4):
            y_idx = y + y_direction[idx]
            x_idx = x + x_direction[idx]

            if 0 <= y_idx < N and 0 <= x_idx < N:
                if not visited[y_idx][x_idx]:
                    if L <= abs(countries[y][x] - countries[y_idx][x_idx]) <= R:
                        deq.append([y_idx, x_idx])
                        visited[y_idx][x_idx] = True

    change_population(can_move, sums // number_of_people)


N, L, R = map(int, sys.stdin.readline().split())
countries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

limit = N * N
days = 0
moved = [[False] * N for _ in range(N)]
while True:
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for y_i in range(N):
        for x_i in range(N):
            if not visited[y_i][x_i]:
                cnt += 1
                bfs([y_i, x_i])

    # 이동을 할 수 없으면 cnt 의 갯수는 총 국가 수가 된다
    if limit == cnt:
        break
    days += 1

print(days)

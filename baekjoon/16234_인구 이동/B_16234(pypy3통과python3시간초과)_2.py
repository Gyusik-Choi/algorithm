import sys
from collections import deque


def bfs(start):
    deq = deque()
    deq.append(start)

    can_move = []
    sums = 0
    number_of_people = 0

    while deq:
        [y, x] = deq.popleft()
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

    if len(can_move) > 1:
        avg = sums // number_of_people
        for can in can_move:
            countries[can[0]][can[1]] = avg
        return True
    else:
        return False


N, L, R = map(int, sys.stdin.readline().split())
countries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

y_direction = [-1, 0, 1, 0]
x_direction = [0, 1, 0, -1]

limit = N * N
days = 0

while True:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for y_i in range(N):
        for x_i in range(N):
            if not visited[y_i][x_i]:
                visited[y_i][x_i] = True
                if bfs([y_i, x_i]):
                    flag = True

    if not flag:
        break
    days += 1

sys.stdout.write(str(days))

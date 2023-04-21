from collections import deque


def play_dummy():
    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    time = 0
    direction = 1

    y = 0
    x = 0

    move = deque()
    move.append([0, 0])

    while True:
        time += 1

        y, x = y_value[direction] + y, x_value[direction] + x

        # 이동할 위치의 이동 불가능
        if 0 > y or y >= N or 0 > x or x >= N:
            break

        # 자기 자신
        if board[y][x] == 1:
            break

        # 사과가 없음
        # 사과가 없어서 꼬리 줄여야 한다
        if not board[y][x]:
            tail_y, tail_x = move.popleft()
            board[tail_y][tail_x] = 0

        board[y][x] = 1
        move.append([y, x])

        # 방향 전환 정보 없음
        if not change_direction_info:
            continue

        # 방향 전환 X
        if time < change_direction_info[0][0]:
            continue

        t, d = change_direction_info.popleft()

        if d == 'L':
            direction = (direction + 3) % 4
        else:
            direction = (direction + 1) % 4

    return time


N = int(input())
K = int(input())

# 빈칸 0, 뱀 1, 사과 2
board = [[0] * N for _ in range(N)]
board[0][0] = 1
for _ in range(K):
    A, B = map(int, input().split())
    board[A - 1][B - 1] = 2

L = int(input())
change_direction_info = deque()
for _ in range(L):
    X, C = input().split()
    X = int(X)
    change_direction_info.append([X, C])

print(play_dummy())

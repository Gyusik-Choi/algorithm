from collections import deque


def change_direction(current_direction, direction):
    if direction == 'L':
        return (current_direction - 1) % 4
    return (current_direction + 1) % 4


def start_game(b):
    cnt = 0
    current = 1
    y_cur = 0
    x_cur = 0
    y_axis = [-1, 0, 1, 0]
    x_axis = [0, 1, 0, -1]

    b[y_cur][x_cur] = 0

    deq = deque()
    deq.append([y_cur, x_cur])

    while True:
        cnt += 1

        y_move = deq[-1][0] + y_axis[current]
        x_move = deq[-1][1] + x_axis[current]

        # 벽에 부딪힘
        if 0 > y_move or y_move >= N or 0 > x_move or x_move >= N:
            return cnt

        # 자기 자신과 부딪힘
        if b[y_move][x_move] == 1:
            return cnt

        if 0 <= y_move < N and 0 <= x_move < N:
            # 사과 없음
            if b[y_move][x_move] == 0:
                y_past, x_past = deq.popleft()
                b[y_past][x_past] = 0
            deq.append([y_move, x_move])
            b[y_move][x_move] = 1

        # https://blockdmask.tistory.com/536
        if isinstance(direction_change_info[cnt], str):
            current = change_direction(current, direction_change_info[cnt])


N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 2

L = int(input())
direction_change_info = [0] * 10001
for _ in range(L):
    X, C = input().split()
    direction_change_info[int(X)] = C

answer = start_game(board)
print(answer)

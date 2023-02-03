from collections import deque


def change_snake_direction(direction, value):
    if direction == 'L':
        return (value - 1) % 4

    return (value + 1) % 4


def is_apple(y, x):
    if not board[y][x]:
        return True

    return False


def is_time_to_change_snake_direction(sec):
    if not snakes[sec]:
        return False

    return True


def is_self(y, x):
    return board[y][x] == 1


def is_wall(y, x):
    return y < 0 or y >= N or x < 0 or x >= N


# 이동할 때마다 벽 or 자신 or 사과
def do_dummy_game(b):
    board[0][0] = 1
    move = deque()
    move.append([0, 0])

    cur_y = 0
    cur_x = 0

    snake_direction = 1

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    answer = 0

    while True:
        answer += 1

        # 이동할 좌표
        cur_y = y_direction[snake_direction] + cur_y
        cur_x = x_direction[snake_direction] + cur_x

        if is_wall(cur_y, cur_x):
            return answer

        if is_self(cur_y, cur_x):
            return answer

        if not is_apple(cur_y, cur_x):
            past_y, past_x = move.popleft()
            board[past_y][past_x] = -1

        if is_time_to_change_snake_direction(answer):
            snake_direction = change_snake_direction(snakes[answer], snake_direction)

        move.append([cur_y, cur_x])
        board[cur_y][cur_x] = 1


N = int(input())
# 빈칸 -1, 사과 0, 뱀 1
board = [[-1] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 0

L = int(input())
snakes = [0] * 10001
for _ in range(L):
    X, C = input().split()
    snakes[int(X)] = C

print(do_dummy_game(board))

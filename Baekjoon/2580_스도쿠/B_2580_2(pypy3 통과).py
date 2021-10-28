import sys


def square_possible(y_idx, x_idx, number):
    y_direction = y_idx // 3 * 3
    x_direction = x_idx // 3 * 3

    for k in range(y_direction, y_direction + 3):
        for l in range(x_direction, x_direction + 3):
            if arr[k][l] == number:
                return False
    return True


def horizontal_possible(x_idx, number):
    for k in range(9):
        if arr[k][x_idx] == number:
            return False
    return True


def vertical_possible(y_idx, number):
    for k in range(9):
        if arr[y_idx][k] == number:
            return False
    return True


def sudoku(cnt):
    if cnt == zeros_length:
        for k in range(9):
            print(*arr[k])
        sys.exit(0)

    y, x = zeros[cnt]

    candidates = []
    for num in range(1, 10):
        if vertical_possible(y, num) and horizontal_possible(x, num) and square_possible(y, x, num):
            candidates.append(num)

    for candidate in candidates:
        arr[y][x] = candidate
        sudoku(cnt + 1)
        arr[y][x] = 0


arr = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zeros.append([i, j])

zeros_length = len(zeros)
sudoku(0)

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0

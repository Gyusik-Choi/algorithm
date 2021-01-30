import sys


def row(y, num):
    for l in range(9):
        if arr[y][l] == num:
            return False
    return True


def col(x, num):
    for l in range(9):
        if arr[l][x] == num:
            return False
    return True


def three_by_three(y, x, num):
    ay = y // 3 * 3
    ax = x // 3 * 3
    for l in range(ay, ay + 3):
        for m in range(ax, ax + 3):
            if arr[l][m] == num:
                return False
    return True


def back_track(cnt):
    if cnt == empty_arr_length:
        return
    for m, n in empty_arr:
        for k in range(1, 10):
            if three_by_three(m, n, k) and col(n, k) and row(m, k):
                arr[m][n] = k
                back_track(cnt + 1)
                arr[m][n] = 0


arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

empty_arr = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            empty_arr.append([i, j])

empty_arr_length = len(empty_arr)
back_track(0)
for i in range(9):
    for j in range(9):
        print(arr[i][j], end=" ")
    print()

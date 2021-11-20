def is_same_color(y_axis, x_axis, num):
    standard = colored_paper[y_axis][x_axis]

    for i in range(y_axis, y_axis + num):
        for j in range(x_axis, x_axis + num):
            if standard != colored_paper[i][j]:
                return False

    return True


def divide_and_conquer(y, x, n):
    global white, blue

    if is_same_color(y, x, n):
        if colored_paper[y][x] == 0:
            white += 1
        else:
            blue += 1
    else:
        divide_and_conquer(y, x, n // 2)
        divide_and_conquer(y, x + n // 2, n // 2)
        divide_and_conquer(y + n // 2, x, n // 2)
        divide_and_conquer(y + n // 2, x + n // 2, n // 2)


N = int(input())
colored_paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
divide_and_conquer(0, 0, N)
print(white)
print(blue)


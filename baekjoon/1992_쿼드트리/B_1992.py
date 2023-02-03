def is_same_number(y_axis, x_axis, num):
    target = quad_tree[y_axis][x_axis]

    for i in range(y_axis, y_axis + num):
        for j in range(x_axis, x_axis + num):
            if target != quad_tree[i][j]:
                return False

    return True


def divide_and_conquer(y, x, n):
    global answer

    if is_same_number(y, x, n):
        answer += str(quad_tree[y][x])
        return

    answer += "("

    divide_and_conquer(y, x, n // 2)
    divide_and_conquer(y, x + n // 2, n // 2)
    divide_and_conquer(y + n // 2, x, n // 2)
    divide_and_conquer(y + n // 2, x + n // 2, n // 2)

    answer += ")"


N = int(input())
quad_tree = [list(map(int, input())) for _ in range(N)]
answer = ""
divide_and_conquer(0, 0, N)
print(answer)

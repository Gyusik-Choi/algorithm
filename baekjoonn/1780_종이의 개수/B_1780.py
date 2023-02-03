import sys


def is_same_color(y_axis, x_axis, number):
    target = matrix[y_axis][x_axis]

    for i in range(y_axis, y_axis + number):
        for j in range(x_axis, x_axis + number):
            if matrix[i][j] != target:
                return False

    return True


def divide_and_conquer(y, x, n):
    global answer

    if is_same_color(y, x, n):
        # matrix 값을 조건문으로 -1인지 0인지 1인지 구분하지 않고
        # answer 배열에 0, 1, 2번 인덱스에 -1, 0, 1의 개수를 구했다
        # 이를 위해 matrix 의 값에서 1을 더해주면 인덱스에 맞출 수 있다
        answer[matrix[y][x] + 1] += 1
        return

    divide_and_conquer(y, x, n // 3)
    divide_and_conquer(y, x + n // 3, n // 3)
    divide_and_conquer(y, x + n // 3 + n // 3, n // 3)

    divide_and_conquer(y + n // 3, x, n // 3)
    divide_and_conquer(y + n // 3, x + n // 3, n // 3)
    divide_and_conquer(y + n // 3, x + n // 3 + n // 3, n // 3)

    divide_and_conquer(y + n // 3 + n // 3, x, n // 3)
    divide_and_conquer(y + n // 3 + n // 3, x + n // 3, n // 3)
    divide_and_conquer(y + n // 3 + n // 3, x + n // 3 + n // 3, n // 3)


N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = [0, 0, 0]

divide_and_conquer(0, 0, N)
print(answer[0])
print(answer[1])
print(answer[2])

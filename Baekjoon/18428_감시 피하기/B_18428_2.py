def reset_o(hall, combination):
    for idx, c in enumerate(combination):
        y = empty[c][0]
        x = empty[c][1]
        hall[y][x] = 'X'


def set_o(hall, combination):
    for idx, c in enumerate(combination):
        y = empty[c][0]
        x = empty[c][1]
        hall[y][x] = 'O'


def dfs(hallway, start):
    for idx in range(4):
        # 0 상, 1 우, 2 하, 3 좌
        if idx == 0:
            y_direction = -1
            x_direction = 0
        elif idx == 1:
            y_direction = 0
            x_direction = 1
        elif idx == 2:
            y_direction = 1
            x_direction = 0
        else:
            y_direction = 0
            x_direction = -1

        # 선생님 출발점
        y = start[0]
        x = start[1]

        while True:
            y += y_direction
            x += x_direction

            if 0 <= y < N and 0 <= x < N:
                if hallway[y][x] == 'S':
                    return False

                if hallway[y][x] == 'O':
                    break
            else:
                break

    return True


def get_answer(hall, combination):
    set_o(hall, combination)

    for teacher in teachers:
        if not dfs(hall, teacher):
            reset_o(hall, combination)
            return False

    reset_o(hall, combination)
    return True


def combinations(idx, num, limit):
    if idx == limit:
        combs.append(temp_comb[:])
    else:
        for n in range(num, len(empty)):
            temp_comb.append(n)
            combinations(idx + 1, n + 1, limit)
            temp_comb.pop()


N = int(input())
corridor = [list(input().split()) for _ in range(N)]

empty = []
teachers = []
for i, row in enumerate(corridor):
    for j, item in enumerate(row):
        if item == 'X':
            empty.append([i, j])
        elif item == 'T':
            teachers.append([i, j])

combs = []
temp_comb = []
combinations(0, 0, 3)

answer_flag = False
for i, comb in enumerate(combs):
    if get_answer(corridor, comb):
        answer_flag = True
        break

if answer_flag:
    print('YES')
else:
    print('NO')

# 반례 참고
# https://www.acmicpc.net/board/view/75916

# 5
# X X S X X
# X X X X X
# S X T X S
# X X X X X
# X X S X X
# NO

# 5
# X T X T X
# T X S X T
# X S S S X
# T X S X X
# X T X X X
# YES

# 5
# X S S S X
# T X X S X
# X T X S X
# X X T X S
# X X X T X
# YES

import copy


def dfs(new_copied_corridor, start, idx):
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

    stack = [start]
    while stack:
        [y_idx, x_idx] = stack.pop()

        y_axis = y_idx + y_direction
        x_axis = x_idx + x_direction

        if 0 <= y_axis < N and 0 <= x_axis < N:
            if new_copied_corridor[y_axis][x_axis] == 'S':
                return False

            if new_copied_corridor[y_axis][x_axis] == 'O':
                return True

            if new_copied_corridor[y_axis][x_axis] == 'X':
                new_copied_corridor[y_axis][x_axis] = 'T'
                stack.append([y_axis, x_axis])

    return True


def get_answer(copied_corridor, comb):
    for j, c in enumerate(comb):
        y = empty[c][0]
        x = empty[c][1]
        copied_corridor[y][x] = 'O'

    for teacher in teachers:
        for k in range(4):
            new_copied_corridor = copy.deepcopy(copied_corridor)
            if not dfs(new_copied_corridor, teacher, k):
                return False

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
    copied_corridor = copy.deepcopy(corridor)
    if get_answer(copied_corridor, comb):
        answer_flag = True
        break

if answer_flag:
    print('YES')
else:
    print('NO')

# 반례 참고
# https://www.acmicpc.net/board/view/75916

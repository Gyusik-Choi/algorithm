import copy


def dfs(copied_corridor, start):
    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    stack = [start]
    while stack:
        [y_idx, x_idx] = stack.pop()

        for k in range(4):
            y_axis = y_idx + y_direction[k]
            x_axis = x_idx + x_direction[k]

            if 0 <= y_axis < N and 0 <= x_axis < N:
                if copied_corridor[y_axis][x_axis] == 'S':
                    return False

                if copied_corridor[y_axis][x_axis] == 'X':
                    copied_corridor[y_axis][x_axis] = 'T'
                    stack.append([y_axis, x_axis])

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

answer_flag = True
for i, comb in enumerate(combs):
    copied_corridor = copy.deepcopy(corridor)
    for j, c in enumerate(comb):
        y = empty[c][0]
        x = empty[c][1]
        copied_corridor[y][x] = 'O'

    for teacher in teachers:
        if not dfs(copied_corridor, teacher):
            answer_flag = False
            break

    if answer_flag:
        break

if answer_flag:
    print('YES')
else:
    print('NO')

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
# Yes

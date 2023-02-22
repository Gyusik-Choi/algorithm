def search(hall, start, direction):
    y, x = start

    y += y_value[direction]
    x += x_value[direction]

    if 0 > y or y >= N or 0 > x or x >= N:
        return False

    if hall[y][x] == 'O':
        return False

    if hall[y][x] == 'S':
        return True

    return search(hall, [y, x], direction)


def search_student(hall, teachers):
    for t in teachers:
        for d in range(4):
            if search(hall, t, d):
                return True

    return False


def reset_obstacle(hall, obstacle):
    for o in obstacle:
        y, x = empty_space[o]

        hall[y][x] = 'X'


def set_obstacle(hall, obstacle):
    for o in obstacle:
        y, x = empty_space[o]

        hall[y][x] = 'O'


def get_combinations(cnt, cnt_limit, num, num_limit, arr):
    if cnt == cnt_limit:
        empty_space_combinations.append(arr[:])
        return

    for n in range(num, num_limit):
        arr.append(n)
        get_combinations(cnt + 1, cnt_limit, n + 1, num_limit, arr)
        arr.pop()


N = int(input())
corridor = [list(input().split()) for _ in range(N)]

empty_space = []
teacher = []
student = []

for i in range(N):
    for j in range(N):
        if corridor[i][j] == 'X':
            empty_space.append([i, j])
        elif corridor[i][j] == 'T':
            teacher.append([i, j])
        else:
            student.append([i, j])

empty_space_combinations = []

get_combinations(0, 3, 0, len(empty_space), [])

y_value = [-1, 0, 1, 0]
x_value = [0, 1, 0, -1]

is_find = True

for comb in empty_space_combinations:
    set_obstacle(corridor, comb)

    if not search_student(corridor, teacher):
        is_find = False
        break

    reset_obstacle(corridor, comb)

print('YES' if not is_find else 'NO')

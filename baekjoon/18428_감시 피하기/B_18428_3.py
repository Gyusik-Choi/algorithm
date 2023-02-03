def dfs(copied_hallway, y, x, y_direction_value, x_direciton_value):
    y_idx = y + y_direction_value
    x_idx = x + x_direciton_value

    if 0 <= y_idx < N and 0 <= x_idx < N:
        if copied_hallway[y_idx][x_idx] == 'O':
            return True

        if copied_hallway[y_idx][x_idx] == 'S':
            return False
    else:
        return True

    return dfs(copied_hallway, y_idx, x_idx, y_direction_value, x_direciton_value)


def reset_obstacle(copied_hallway, combination):
    for idx, c in enumerate(combination):
        y, x = empty[c]
        copied_hallway[y][x] = 'X'


def set_obstacle(copied_hallway, combination):
    for idx, c in enumerate(combination):
        y, x = empty[c]
        copied_hallway[y][x] = 'O'


def monitor(hall):
    for m in range(len(teacher)):
        teacher_y, teacher_x = teacher[m]

        for direction in range(4):
            if not dfs(hall, teacher_y, teacher_x, y_value[direction], x_value[direction]):
                return False

    return True


def do_monitor(all_combinations):
    for idx, comb in enumerate(all_combinations):
        set_obstacle(hallway, comb)

        if monitor(hallway):
            return True

        reset_obstacle(hallway, comb)

    return False


def get_obstacle_combination(limit, cnt, idx, temp_comb):
    if cnt == limit:
        combinations.append(temp_comb[:])
        # 여기서 return 을 해주지 않으면 시간 초과가 발생 한다
        # return 이 없으면 append 이후 for 문으로 가기 때문에
        # for 문을 추가적으로 불필요하게 돌게 된다
        return

    for k in range(idx, len(empty)):
        temp_comb.append(k)
        get_obstacle_combination(limit, cnt + 1, k + 1, temp_comb)
        temp_comb.pop()


N = int(input())
hallway = []
teacher = []
empty = []

for i in range(N):
    h = list(input().split())
    hallway.append(h)

    for j in range(N):
        if h[j] == 'T':
            teacher.append([i, j])
        elif h[j] == 'X':
            empty.append([i, j])

y_value = [-1, 0, 1, 0]
x_value = [0, 1, 0, -1]

combinations = []
get_obstacle_combination(3, 0, 0, [])

if do_monitor(combinations):
    print('YES')
else:
    print('NO')

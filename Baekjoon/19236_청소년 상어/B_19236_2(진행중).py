import copy


def possible_shark_move_list(shark) -> list:
    y, x = shark
    shark_move_list = []

    shark_direction = space[y][x][1]
    temp_shark_y = y
    temp_shark_x = x

    # 최대 3번 까지 이동 가능
    for k in range(3):
        temp_y = temp_shark_y + y_value[shark_direction - 1]
        temp_x = temp_shark_x + x_value[shark_direction - 1]

        if 0 > temp_y or temp_y >= N or 0 > temp_x or temp_x >= N:
            break

        shark_move_list.append([temp_y, temp_x])
        temp_shark_y = temp_y
        temp_shark_x = temp_x

    return shark_move_list


def find_shark(copied_space) -> list:
    for m in range(4):
        for n in range(4):
            if copied_space[m][n][0] == 0:
                return [m, n]


def get_fish_idx_to_move(copied_space, y, x) -> list:
    origin_direction = copied_space[y][x][1] - 1

    for k in range(8):
        idx = (k + origin_direction) % 8

        y_idx = y_value[idx] + y
        x_idx = x_value[idx] + x

        # 공간 범위 안에 있는지
        if 0 <= y_idx < N and 0 <= x_idx < N:
            # 상어가 없는지
            if copied_space[y_idx][x_idx][0]:
                # y축, x축, 물고기 방향 변환할 값
                return [y_idx, x_idx, k]

    return []


def change_fish(fish1, fish2):
    space[fish1], space[fish2] = space[fish2], space[fish1]


def change_fish_direction_value(fish_idx, fish_direction):
    space[fish_idx[0]][fish_idx[1]][1] = fish_direction


def find_fish(copied_space, fish_num) -> list:
    for m in range(4):
        for n in range(4):
            if copied_space[m][n][0] == fish_num:
                return [m, n]

    return []


# def move_shark(fish_eat_num) -> bool:
#     for shark_move in shark_move_list:
#         y, x = shark_move
#
#         # 기존 위치 빈칸 처리
#         space[y][x][0] = -1
#
#         # 이동
#
#
#         # fish_eat_num 값 증가
#         fish_eat_num += 1

def move_shark(copied_space, current_shark, future_shark):
    c_y, c_x = current_shark
    f_y, f_x = future_shark

    copied_space[c_y][c_x][0] = -1
    copied_space[f_y][f_x][0] = 0


def move_fish(copied_space):
    # 첫 상어 이동 후 남은 물고기 15
    for k in range(1, 16):
        fish_idx = find_fish(copied_space, k)

        if not fish_idx:
            continue

        # 원래 방향 부터 최대 8번
        # 물고기 이동 가능한 위치 찾기
        fish_idx_to_move = get_fish_idx_to_move(copied_space, fish_idx[0], fish_idx[1])

        if not fish_idx_to_move:
            continue

        # 물고기 방향 값 변환
        # (이동할 방향의 y축, x축이 아니라 현재 물고기 위치의 y축, x축을 전달)
        change_fish_direction_value(fish_idx, fish_idx_to_move[2])
        change_fish(fish_idx, fish_idx_to_move[:2])


def move(fish_eat_num):
    global answer

    copied_space = copy.deepcopy(space)

    while True:
        move_fish(copied_space)
        # if not move_shark(0):
        #     break
        shark = find_shark(copied_space)
        shark_move_list = possible_shark_move_list(shark)

        if not shark_move_list:
            break

        for shark_move in shark_move_list:
            move_shark(copied_space, shark, shark_move)

            if fish_eat_num + 1 > answer:
                answer = fish_eat_num + 1

            move(fish_eat_num + 1)


def move_first_shark():
    space[0][0][0] = 0


def brute_force():
    move_first_shark()
    move(0)


space = [[] * 4 for _ in range(4)]
N = 4

for i in range(4):
    fish_info = list(map(int, input().split()))

    for j in range(0, 8, 2):
        space[i].append([fish_info[j], fish_info[j + 1]])

y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
x_value = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 1
brute_force()

# 물고기 1 ~ 16
# 상어 0
# 빈칸 -1

# 첫 상어 이동

# 물고기 이동
# 상어 이동
# 후보군 모두 탐색

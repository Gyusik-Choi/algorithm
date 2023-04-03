import copy


def move(info, sums):
    global max_sums

    new_info = copy.deepcopy(info)

    # 물고기 이동
    move_fish(new_info)

    # 상어 위치
    shark: list = find_shark(new_info)

    # 상어 이동 가능 여부
    shark_move_list: list = find_shark_move(new_info, shark)

    # 1) 상어 이동 불가능 하면 종료
    if not shark_move_list:
        return

    # 2) 상어 이동 가능 하면 탐색
    for future_shark in shark_move_list:
        original_num = move_shark(new_info, shark, future_shark)

        max_sums = max(max_sums, sums + original_num)

        move(new_info, sums + original_num)

        revert_move_shark(new_info, shark, future_shark, original_num)


def move_fish(info):
    for fish_num in range(1, 17):
        fish_location: list = find_fish_location(info, fish_num)

        if not fish_location:
            continue

        fish_can_move: list = find_fish_can_move(info, fish_location)

        if not fish_can_move:
            continue

        fish_y, fish_x = fish_location
        fish_direction = fish_can_move.pop()
        info[fish_y][fish_x][1] = fish_direction

        switch_fish(info, fish_location, fish_can_move)


def find_fish_location(info, fish_num) -> list:
    for m in range(4):
        for n in range(4):
            if info[m][n][0] == fish_num:
                return [m, n]

    return []


def find_fish_can_move(info, fish) -> list:
    y, x = fish
    fish_direction = info[y][x][1] - 1

    y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
    x_value = [0, -1, -1, -1, 0, 1, 1, 1]

    for k in range(8):
        # fish_direction = (k + fish_direction) % 8
        # fish_direction 은 위처럼 누적이 아니라 기존 값에서 바꿔야 한다
        direction = (k + fish_direction) % 8

        y_idx, x_idx = y_value[direction] + y, x_value[direction] + x

        # 공간의 경계 넘는 칸
        if 0 > y_idx or y_idx >= 4 or 0 > x_idx or x_idx >= 4:
            continue

        # 상어가 있는 칸
        if not info[y_idx][x_idx][0]:
            continue

        # y, x, 방향
        # 물고기 방향을 바꿔야 해서 해당 값도 리턴에 포함
        # fish_direction 은 1 ~ 8 이라
        # 0 ~ 7 인덱스 값을 갖는 y_value, x_value 에 맞춰서
        # 1을 빼줬고
        # 리턴 해줄 때는 1을 더해서 1 ~ 8 사이의 값이 되도록 한다
        return [y_idx, x_idx, direction + 1]

    return []


def switch_fish(info, cur, post):
    # 빈칸인 경우도 있다
    info[cur[0]][cur[1]], info[post[0]][post[1]] = info[post[0]][post[1]], info[cur[0]][cur[1]]


def find_shark_move(info, shark) -> list:
    y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
    x_value = [0, -1, -1, -1, 0, 1, 1, 1]

    shark_y, shark_x = shark
    shark_direction = info[shark_y][shark_x][1] - 1

    shark_move = []

    # 상어는 현재 위치 기준 최대 3번 까지 이동 가능
    for k in range(3):
        shark_y, shark_x = y_value[shark_direction] + shark_y, x_value[shark_direction] + shark_x

        if 0 > shark_y or shark_y >= 4 or 0 > shark_x or shark_x >= 4:
            continue

        if info[shark_y][shark_x][0] <= 0:
            continue

        shark_move.append([shark_y, shark_x])

    return shark_move


def find_shark(info) -> list:
    for m in range(4):
        for n in range(4):
            if not info[m][n][0]:
                return [m, n]

    return []


def move_shark(info, cur, post):
    original_post_num = info[post[0]][post[1]][0]

    info[cur[0]][cur[1]][0], info[post[0]][post[1]][0] = -1, 0

    return original_post_num


def revert_move_shark(info, cur, pre, original_num):
    info[cur[0]][cur[1]][0], info[pre[0]][pre[1]][0] = 0, original_num


fish_info = []

for _ in range(4):
    info_row = list(map(int, input().split()))
    temp_info = []

    for i in range(0, 8, 2):
        a, b = info_row[i], info_row[i + 1]
        temp_info.append([a, b])

    fish_info.append(temp_info)

max_sums = fish_info[0][0][0]

fish_info[0][0][0] = 0

move(fish_info, max_sums)
print(max_sums)

# 물고기 1 ~ 16
# 상어 0
# 빈칸 -1

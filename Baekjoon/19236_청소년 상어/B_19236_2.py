import copy


def get_fish_num(copied_space, shark):
    return copied_space[shark[0]][shark[1]][0]


def check_answer(fish_eat_num, fish_num):
    global answer
    answer = max(answer, fish_eat_num + fish_num)


def eat_fish(copied_space, shark):
    copied_space[shark[0]][shark[1]][0] = 0


def move_fish(copied_space):
    # 첫 상어 이동 후 남은 물고기 15 마리
    # 1 ~ 16 사이의 물고기 탐색
    for k in range(1, 17):
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
        change_fish_direction_value(copied_space, fish_idx, fish_idx_to_move[2])
        change_fish(copied_space, fish_idx, fish_idx_to_move[:2])


def find_fish(copied_space, fish_num) -> list:
    for m in range(4):
        for n in range(4):
            if copied_space[m][n][0] == fish_num:
                return [m, n]

    return []


def get_fish_idx_to_move(copied_space, y, x) -> list:
    origin_direction = copied_space[y][x][1]

    for k in range(8):
        idx = (k + origin_direction) % 8

        y_idx = y_value[idx] + y
        x_idx = x_value[idx] + x

        # 공간 범위 안에 있는지
        if 0 <= y_idx < N and 0 <= x_idx < N:
            # 상어가 없는지
            if copied_space[y_idx][x_idx][0]:
                # y축, x축, 물고기 방향 변환할 값
                return [y_idx, x_idx, idx]

    return []


def change_fish_direction_value(copied_space, fish_idx, fish_direction):
    copied_space[fish_idx[0]][fish_idx[1]][1] = fish_direction


def change_fish(copied_space, fish1, fish2):
    copied_space[fish1[0]][fish1[1]], copied_space[fish2[0]][fish2[1]] = copied_space[fish2[0]][fish2[1]], copied_space[fish1[0]][fish1[1]]


def possible_shark_move_list(copied_space, shark) -> list:
    y, x = shark
    shark_move_list = []

    shark_direction = copied_space[y][x][1]

    # 최대 3번 까지 이동 가능
    for k in range(3):
        temp_y = y + y_value[shark_direction]
        temp_x = x + x_value[shark_direction]

        # if 0 > temp_y or temp_y >= N or 0 > temp_x or temp_x >= N:
            # break
        # 위와 같이 break 를 걸지 않고 3번을 다 탐색 한다
        if 0 <= temp_y < N and 0 <= temp_x < N and copied_space[temp_y][temp_x][0] > 0:
            shark_move_list.append([temp_y, temp_x])

        y = temp_y
        x = temp_x

    return shark_move_list


def move_shark(copied_space, current_shark):
    c_y, c_x = current_shark

    # 빈칸
    copied_space[c_y][c_x][0] = -1
    copied_space[c_y][c_x][1] = -1


def move(new_space, fish_eat_num, shark):
    copied_space = copy.deepcopy(new_space)

    # 아래의 move_shark 에서 상어가 물고기 먹는 것을 처리하면
    # 만약에 shark_move_list 가 없어서 for 문을 돌지 못하고
    # 이전의 for 문으로 돌아왔을 때 (이전의 실행 컨텍스트로 돌아왔을 때)
    # 배열은 참조 방식이라
    # 이미 먹은 물고기 정보가 초기화 되지 못하고 남게 된다
    # 이를 막기 위해
    # 상어가 물고기 먹는 것을 여기서 처리 하고
    # 아래의 move_shark 에서는 상어의 이동을 처리 한다
    fish_num = get_fish_num(copied_space, shark)
    check_answer(fish_eat_num, fish_num)
    eat_fish(copied_space, shark)

    move_fish(copied_space)

    shark_move_list = possible_shark_move_list(copied_space, shark)

    for shark_move in shark_move_list:
        move_shark(copied_space, shark)
        move(copied_space, fish_eat_num + fish_num, shark_move)


space = [[] * 4 for _ in range(4)]
N = 4

for i in range(4):
    fish_info = list(map(int, input().split()))

    for j in range(0, 8, 2):
        # 방향 값을 -1 빼서 넣는다
        space[i].append([fish_info[j], fish_info[j + 1] - 1])

y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
x_value = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0
move(space, 0, [0, 0])
print(answer)

# 물고기 1 ~ 16
# 상어 0
# 빈칸 -1

# 첫 상어 이동
# 물고기 이동
# 상어 이동
# 후보군 모두 탐색

# https://www.acmicpc.net/board/view/58205
# 반례
# 7 6 2 6 15 7 9 3
# 3 5 1 4 14 1 10 6
# 6 4 13 3 4 6 11 1
# 16 5 8 7 5 2 12 2
# => 88
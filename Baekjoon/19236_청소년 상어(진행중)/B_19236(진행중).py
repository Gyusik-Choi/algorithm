import copy


def switch_fish(visited, visited_sea_way, fish_y, fish_x, target_fish_y, target_fish_x):
    visited[fish_y][fish_x], visited[target_fish_y][target_fish_x] = visited[target_fish_y][target_fish_x], visited[fish_y][fish_x]
    visited_sea_way[fish_y][fish_x], visited_sea_way[target_fish_y][target_fish_x] = visited_sea_way[target_fish_y][target_fish_x], visited_sea_way[fish_y][fish_x]


def is_fish_possible_to_move(visited, fish_way, y_idx, x_idx):
    # 1번은 이미 함수 호출 전에 검사했음
    for _ in range(7):
        y = y_idx + dy[fish_way]
        x = x_idx + dx[fish_way]

        # 빈칸도 이동가능
        if 0 <= y < 4 and 0 <= x < 4 and visited[y][x] >= 0:
            return [y, x]

        fish_way = (fish_way + 1) % 8

    return False


def find_fish_to_move(visited):
    global current_fish_num

    for m in range(4):
        for n in range(4):
            if visited[m][n] == current_fish_num:
                return [m, n]

    if current_fish_num < 16:
        current_fish_num += 1
        return find_fish_to_move(visited)


def fish_move(visited, visited_way):
    global current_fish_num

    while current_fish_num <= 16:
        find_fish_to_move_result = find_fish_to_move(visited)
        if find_fish_to_move_result is None:
            break

        fish_y, fish_x = find_fish_to_move_result
        fish_way = visited_way[fish_y][fish_x] - 1

        y_idx = fish_y + dy[fish_way]
        x_idx = fish_x + dx[fish_way]

        # 공간의 경계를 넘는지 혹은 상어가 있는지
        if 0 <= y_idx < 4 and 0 <= x_idx < 4 and visited[y_idx][x_idx] != -1:
            switch_fish(visited, visited_way, fish_y, fish_x, y_idx, x_idx)
        else:
            while True:
                result = is_fish_possible_to_move(visited, (fish_way + 1) % 8, y_idx, x_idx)
                if not result:
                    break

                switch_fish(visited, visited_way, fish_y, fish_x, result[0], result[1])
                break

        current_fish_num += 1
    current_fish_num = 1


def get_possible_shark_move(s_y, s_x, s, shark_way):
    possible_shark_move_list = []

    for _ in range(4):
        y = s_y + dy[shark_way]
        x = s_x + dx[shark_way]

        if 0 <= y < 4 and 0 <= x < 4:
            if s[y][x] > 0:
                possible_shark_move_list.append([y, x])
            s_y = y
            s_x = x
        else:
            break
    # print(possible_shark_move_list)
    return possible_shark_move_list


def back_tracking_shark(s_y, s_x, s, s_way, num):
    global max_num

    copied_sea, copied_sea_way = copy.deepcopy(s), copy.deepcopy(s_way)

    # 원래 물고기 값
    original_copied_sea_value = copied_sea[s_y][s_x]
    # 상어가 온 자리는 빈칸 -1
    copied_sea[s_y][s_x] = -1
    # 물고기 번호 합 최대값 갱신 가능할 경우 갱신
    max_num = max(max_num, num + original_copied_sea_value)
    # 물고기 이동
    fish_move(copied_sea, copied_sea_way)

    shark_way = copied_sea_way[s_y][s_x] - 1

    possible_shark_move = get_possible_shark_move(s_y, s_x, copied_sea, shark_way)

    for k in range(len(possible_shark_move)):
        # 상어가 떠나면서 빈칸 0
        copied_sea[s_y][s_x] = 0
        # 상어가 이동할 수 있는 y, x 좌표
        y, x = possible_shark_move[k]
        # 이어서 탐색
        back_tracking_shark(y, x, copied_sea, copied_sea_way, num + original_copied_sea_value)


fish_info = [list(map(int, input().split())) for _ in range(4)]
sea = [[0] * 4 for _ in range(4)]
sea_way = [[0] * 4 for _ in range(4)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    cnt = 0
    for j in range(0, 8, 2):
        fish_num = fish_info[i][j]
        fish_direction = fish_info[i][j + 1]
        sea[i][j - cnt] = fish_num
        sea_way[i][j - cnt] = fish_direction
        cnt += 1

max_num = 0
# 상어 y 좌표
shark_y = 0
# 상어 x 좌표
shark_x = 0
# 찾을 물고기 번호
current_fish_num = 1

back_tracking_shark(shark_y, shark_x, sea, sea_way, 0)
print(max_num)

# 상어가 이동할 수 있는 칸이 여러개 일때 어디로 갈지 어떻게 결정?
# => 백트래킹

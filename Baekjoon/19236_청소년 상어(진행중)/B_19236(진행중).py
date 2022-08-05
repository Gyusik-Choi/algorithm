import copy


def switch_fish(visited, visited_sea_way, fish_y, fish_x, target_fish_y, target_fish_x):
    visited[fish_y][fish_x], visited[target_fish_y][target_fish_x] = visited[target_fish_y][target_fish_x], visited[fish_y][fish_x]
    visited_sea_way[fish_y][fish_x], visited_sea_way[target_fish_y][target_fish_x] = visited_sea_way[target_fish_y][target_fish_x], visited_sea_way[fish_y][fish_x]


def is_fish_possible_to_move(visited, fish_way, y_idx, x_idx):
    cnt_num = 0

    # 1개는 이미 함수 호출 이전에 검사함
    while cnt_num < 7:
        y = y_idx + dy[fish_way]
        x = x_idx + dx[fish_way]

        if 0 <= y < 4 and 0 <= x < 4 and visited[y][x] > 0:
            return [y, x]
        else:
            cnt_num += 1
            fish_way = (fish_way + 1) % 8

    return False


def find_fish_to_move(visited, current_fish_num):
    for m in range(4):
        for n in range(4):
            if visited[m][n] == current_fish_num:
                return [m, n]

    if current_fish_num < 16:
        current_fish_num += 1
        return find_fish_to_move(visited, current_fish_num)


def fish_move(visited, visited_way):
    current_fish_num = 1

    while current_fish_num <= 16:
        find_fish_to_move_result = find_fish_to_move(visited, current_fish_num)
        if find_fish_to_move_result is None:
            break

        fish_y, fish_x = find_fish_to_move_result

        fish_way = visited_way[fish_y][fish_x]
        fish_way -= 1

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


def get_possible_shark_move(s_y, s_x, s, s_way, shark_way, possible_list):
    y = s_y + dy[shark_way]
    x = s_x + dx[shark_way]

    if 0 <= y < 4 and 0 <= x < 4 and 0 < s[y][x]:
        possible_list.append([y, x])
        get_possible_shark_move(y, x,  s, s_way, shark_way, possible_list)

    return possible_list


def back_tracking_shark(s_y, s_x, s, s_way, num):
    global max_num

    copied_sea, copied_sea_way = copy.deepcopy(s), copy.deepcopy(s_way)
    fish_move(copied_sea, copied_sea_way)
    shark_way = sea_way[s_y][s_x]
    shark_way -= 1
    possible_shark_move = get_possible_shark_move(s_y, s_x, copied_sea, copied_sea_way, shark_way, [])

    for k in range(len(possible_shark_move)):
        # 상어가 떠난 자리는 빈칸 0
        copied_sea[s_y][s_x] = 0
        # 상어가 이동할 수 있는 y, x 좌표
        y, x = possible_shark_move[k]
        # 원래 물고기 값
        original_visited_value = copied_sea[y][x]
        # 상어 이동
        copied_sea[y][x] = -1
        # 물고기 번호 합 최대값 갱신 가능할 경우 갱신
        max_num = max(max_num, num + original_visited_value)
        # 이어서 탐색
        back_tracking_shark(y, x, copied_sea, copied_sea_way, num + original_visited_value)


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

# 0, 0 의 물고기
# 상어는 -1, 빈칸은 0
max_num = 0
max_num += sea[0][0]

shark_y = 0
shark_x = 0
sea[0][0] = -1

back_tracking_shark(0, 0, sea, sea_way, 0)

print(max_num)

# 상어가 이동할 수 있는 칸이 여러개 일때 어디로 갈지 어떻게 결정?
# => 백트래킹

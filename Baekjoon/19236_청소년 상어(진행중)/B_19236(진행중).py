import copy


def switch_fish(fish_y, fish_x, target_fish_y, target_fish_x):
    sea[fish_y][fish_x], sea[target_fish_y][target_fish_x] = sea[target_fish_y][target_fish_x], sea[fish_y][fish_x]


def is_fish_possible_to_move(fish_way, y_idx, x_idx):
    cnt_num = 0

    # 1개는 이미 함수 호출 이전에 검사함
    while cnt_num < 7:
        y = y_idx + dy[fish_way]
        x = x_idx + dx[fish_way]

        if 0 <= y < 4 and 0 <= x < 4 and sea[y][x] == -1:
            return [y, x]
        else:
            cnt_num += 1
            fish_way = (fish_way + 1) % 8

    return False


def find_fish_to_move():
    for m in range(4):
        for n in range(4):
            if sea[m][n] == current_fish_num:
                return [m, n]


def fish_move(visited):
    global current_fish_num

    fish_y, fish_x = find_fish_to_move()

    while current_fish_num <= 16:
        fish_way = sea_way[fish_y][fish_x]
        fish_way -= 1

        y_idx = fish_y + dy[fish_way]
        x_idx = fish_x + dx[fish_way]

        # 공간의 경계를 넘는지 혹은 상어가 있는지
        if 0 <= y_idx < 4 and 0 <= x_idx < 4 and visited[y_idx][x_idx] == -1:
            switch_fish(fish_y, fish_x, y_idx, x_idx)
        else:
            while True:
                result = is_fish_possible_to_move((fish_way + 1) % 8, fish_y, fish_x)
                if not result:
                    break

                switch_fish(fish_y, fish_x, result[0], result[1])


def get_possible_shark_move(s_y, s_x, way, possible_list):
    y = s_y + dy[way]
    x = s_x + dx[way]

    if 0 <= y < 4 and 0 <= x < 4:
        possible_list.append([y, x])
        get_possible_shark_move(y, x, way, possible_list)

    return possible_list


def back_tracking_shark(s_y, s_x, visited, fish_cnt):
    global max_fish_cnt
    fish_move(visited)
    shark_way = sea_way[s_y][s_x]
    shark_way -= 1
    possible_shark_move = get_possible_shark_move(s_y, s_x, shark_way, [])

    for k in range(len(possible_shark_move)):
        y, x = possible_shark_move[k]
        original_visited_value = visited[y][x]
        visited[y][x] = -1
        max_fish_cnt = max(max_fish_cnt, fish_cnt + 1)
        back_tracking_shark(y, x, visited, fish_cnt + 1)
        visited[y][x] = original_visited_value


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

answer = 0
current_fish_num = 1

if fish_info[0][0] == 1:
    current_fish_num = 2

# 0, 0 의 물고기
# 상어는 -1, 빈칸은 0
shark_y = 0
shark_x = 0
sea[0][0] = -1
answer += sea[0][0]

copied_sea = copy.deepcopy(sea)
max_fish_cnt = 1
back_tracking_shark(0, 0, copied_sea, max_fish_cnt)

print(max_fish_cnt)

# 상어가 이동할 수 있는 칸이 여러개 일때 어디로 갈지 어떻게 결정?
# => 백트래킹

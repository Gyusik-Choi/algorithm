import copy


def move(sea, shark, total):
    global max_total

    # 상어 이동
    fish_num = move_shark(sea, shark)

    total += fish_num

    max_total = max(max_total, total)

    # 물고기 이동
    move_fish(sea)

    # 상어 이동 가능한 곳
    shark_can_move = find_shark_can_move(sea, find_shark(sea))

    for i, s in enumerate(shark_can_move):
        move(copy.deepcopy(sea), s, total)


def move_fish(sea):
    for num in range(1, 17):
        # 물고기 찾기
        fish = find_fish(sea, num)

        # 물고기 없으면 다음 번호 물고기 찾기
        if not fish:
            continue

        # 물고기 이동
        # 물고기 현재 위치
        cur_y, cur_x = fish

        # 물고기 이동할 위치 구한다
        next_fish = find_fish_can_move(sea, fish)

        # 물고기 이동할 위치 없음
        if not next_fish:
            continue

        # 물고기 이동할 위치
        next_y, next_x = next_fish

        # 물고기 위치 변경
        sea[cur_y][cur_x], sea[next_y][next_x] = sea[next_y][next_x], sea[cur_y][cur_x]

        
def find_fish(sea, fish_num) -> list:
    for i in range(n):
        for j in range(n):
            if sea[i][j][0] == fish_num:
                return [i, j]

    return []


def find_fish_can_move(sea, fish) -> list:
    y, x = fish
    # 물고기 방향은 0부터 아니라 1부터 시작이라
    # 1을 뺀 값을 구한다
    d = sea[y][x][1] - 1

    for i in range(8):
        new_d = (d + i) % 8
        new_y = y + y_value[new_d]
        new_x = x + x_value[new_d]

        # 칸을 벗어남
        if 0 > new_y or new_y >= n or 0 > new_x or new_x >= n:
            continue

        # 상어
        if not sea[new_y][new_x][0]:
            continue

        # 이동할 곳이 있다
        # 물고기 방향 바꿔준다
        sea[y][x][1] = new_d + 1
        # 이동할 곳 리턴
        return [new_y, new_x]

    # 이동할 곳이 없음
    return []


def get_move_idx(y, x, d) -> list:
    return [y + y_value[d], x + x_value[d]]


def move_shark(sea, shark) -> int:
    cur_shark = find_shark(sea)

    # 맨 처음 상어 이동 했을 경우는
    # 상어가 처음 공간에 들어와서 빈칸으로 할 공간이 없다
    if cur_shark:
        # 기존 상어 위치 빈칸
        sea[cur_shark[0]][cur_shark[1]][0] = -1

    # 상어가 이동할 위치의 물고기 번호
    fish_num = sea[shark[0]][shark[1]][0]

    # 상어 이동
    sea[shark[0]][shark[1]][0] = 0

    return fish_num


def find_shark(sea) -> list:
    for i in range(n):
        for j in range(n):
            if not sea[i][j][0]:
                return [i, j]

    return []


def find_shark_can_move(sea, shark) -> list:
    y, x = shark
    d = sea[y][x][1] - 1

    can_move = []

    # 최대 3곳 이동 가능
    for i in range(3):
        y, x = y + y_value[d], x + x_value[d]

        # 칸 벗어남
        if 0 > y or y >= n or 0 > x or x >= n:
            continue

        # 빈칸
        if sea[y][x][0] == -1:
            continue

        can_move.append([y, x])

    return can_move
        

n = 4
sea_info = []

y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
x_value = [0, -1, -1, -1, 0, 1, 1, 1]

for _ in range(n):
    fish_info = list(map(int, input().split()))
    temp = []

    for idx in range(0, n * 2, 2):
        temp.append([fish_info[idx], fish_info[idx + 1]])

    sea_info.append(temp)

# 빈칸 -1
# 상어 0
# 물고기 1 ~ 16
max_total = 0
move(sea_info, [0, 0], max_total)
print(max_total)

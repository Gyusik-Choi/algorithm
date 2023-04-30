def get_combinations(temp, cnt, cnt_limit, num, num_limit):
    if cnt == cnt_limit:
        empty_combinations.append(temp[:])
        return

    for n in range(num, num_limit):
        temp.append(n)
        get_combinations(temp, cnt + 1, cnt_limit, n + 1, num_limit)
        temp.pop()


def set_obstacles(cor, y, x):
    cor[y][x] = "O"


def reset_obstacles(cor, y, x):
    cor[y][x] = "X"


def dfs(cor, go, direction) -> bool:
    y, x = go
    y_idx, x_idx = y + y_value[direction], x + x_value[direction]

    # 벗어난 영역
    if 0 > y_idx or y_idx >= N or 0 > x_idx or x_idx >= N:
        return True

    # 장애물
    if cor[y_idx][x_idx] == "O":
        return True

    # 학생
    if cor[y_idx][x_idx] == "S":
        return False

    # 빈칸 혹은 선생님
    result = dfs(cor, [y_idx, x_idx], direction)
    return result


def dfs_per_teacher(cor, teachers_info):
    # 선생님 한 명씩
    for k, t in enumerate(teachers_info):
        # 선생님 한 명씩 4방향
        for l in range(4):
            if not dfs(cor, t, l):
                return False

    return True



N = int(input())
corridor = []
students = []
teachers = []
empty = []

for i in range(N):
    row = list(input().split())

    for j, r in enumerate(row):
        if r == "S":
            students.append([i, j])
            continue

        if r == "T":
            teachers.append([i, j])
            continue

        empty.append([i, j])

    corridor.append(row)

empty_combinations = []
get_combinations([], 0, 3, 0, len(empty))

y_value = [-1, 0, 1, 0]
x_value = [0, 1, 0, -1]

is_avoid_possible = False

for comb in empty_combinations:
    # 장애물 설치
    for i, c in enumerate(comb):
        a, b = empty[c]
        set_obstacles(corridor, a, b)

    # 선생님 한 명씩 dfs
    # 한번에 한 방향을 쭉 가야 한다
    # 벗어난 영역, 장애물, 학생일 경우를 제외하고 이동 가능
    # 학생 한 명이라도 발견시 실패
    if dfs_per_teacher(corridor, teachers):
        is_avoid_possible = True
        break

    # 장애물 해제
    for i, c in enumerate(comb):
        a, b = empty[c]
        reset_obstacles(corridor, a, b)

if is_avoid_possible:
    print("YES")
else:
    print("NO")

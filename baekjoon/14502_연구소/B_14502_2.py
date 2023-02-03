from collections import deque
import copy


def count_safe_area(new_laboratory):
    safe_area_cnt = 0
    for n in range(N):
        for m in range(M):
            if new_laboratory[n][m] == 0:
                safe_area_cnt += 1

    return safe_area_cnt


def bfs(new_laboratory, start):
    deq = deque()
    deq.append(start)

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    while deq:
        virus_y, virus_x = deq.popleft()

        for k in range(4):
            virus_y_idx, virus_x_idx = virus_y + y_value[k], virus_x + x_value[k]

            if 0 <= virus_y_idx < N and 0 <= virus_x_idx < M:
                if new_laboratory[virus_y_idx][virus_x_idx] == 0:
                    new_laboratory[virus_y_idx][virus_x_idx] = 2
                    deq.append([virus_y_idx, virus_x_idx])


def set_laboratory(new_laboratory, wall_info):
    for k in range(3):
        wall = wall_info[k]
        y, x = empty_spaces[wall]
        new_laboratory[y][x] = 1


def get_safe_area_cnt(new_laboratory, wall_info):
    set_laboratory(new_laboratory, wall_info)

    for k in range(len(virus)):
        bfs(new_laboratory, virus[k])

    safe_area_cnt = count_safe_area(new_laboratory)
    return safe_area_cnt


def combination(limit, num, cnt, temp_comb):
    if cnt == limit:
        combinations.append(temp_comb[:])
        return

    for k in range(num, len(empty_spaces)):
        temp_comb.append(k)
        combination(limit, k + 1, cnt + 1, temp_comb)
        temp_comb.pop()


N, M = map(int, input().split())
laboratory = []
empty_spaces = []
virus = []
for i in range(N):
    lab = list(map(int, input().split()))
    laboratory.append(lab)

    for j in range(len(lab)):
        if not lab[j]:
            empty_spaces.append([i, j])
        elif lab[j] == 2:
            virus.append([i, j])

visited = [False] * len(empty_spaces)
combinations = []
combination(3, 0, 0, [])

max_safe_area = 0
for idx, comb in enumerate(combinations):
    copied_laboratory = copy.deepcopy(laboratory)
    max_safe_area = max(max_safe_area, get_safe_area_cnt(copied_laboratory, comb))

print(max_safe_area)

from collections import deque
import copy


def get_combinations(temp, cnt, cnt_limit, num, num_limit):
    if cnt == cnt_limit:
        empty_combinations.append(temp[:])
        return

    for n in range(num, num_limit):
        temp.append(n)
        get_combinations(temp, cnt + 1, cnt_limit, n + 1, num_limit)
        temp.pop()


def set_wall(map_info, wall):
    y, x = wall
    map_info[y][x] = 1


def bfs(map_info, virus_info):
    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    deq = deque()

    for v in virus_info:
        deq.append(v)

    while deq:
        y, x = deq.popleft()

        for k in range(4):
            y_idx, x_idx = y + y_value[k], x + x_value[k]

            # 지도 벗어남
            if 0 > y_idx or y_idx >= N or 0 > x_idx or x_idx >= M:
                continue

            # 자신 혹은 벽
            if map_info[y_idx][x_idx] == 2 or map_info[y_idx][x_idx] == 1:
                continue

            map_info[y_idx][x_idx] = 2
            deq.append([y_idx, x_idx])

    return measure_safe_area(map_info)


def measure_safe_area(map_info):
    cnt = 0

    for n, map_row in enumerate(map_info):
        for m, area in enumerate(map_row):
            if not area:
                cnt += 1

    return cnt


N, M = map(int, input().split())
maps = []
empty = []
virus = []

for i in range(N):
    row = list(map(int, input().split()))
    maps.append(row)

    for j, r in enumerate(row):
        if not r:
            empty.append([i, j])
            continue

        if r == 2:
            virus.append([i, j])

empty_combinations = []
get_combinations([], 0, 3, 0, len(empty))
answer = 0

for i, comb in enumerate(empty_combinations):
    new_maps = copy.deepcopy(maps)

    for j, c in enumerate(comb):
        set_wall(new_maps, empty[c])

    answer = max(answer, bfs(new_maps, virus))

print(answer)

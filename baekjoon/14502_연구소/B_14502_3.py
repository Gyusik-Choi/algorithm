from collections import deque
import copy


def count_empty_spaces(visited):
    cnt = 0

    for visit in visited:
        for value in visit:
            if not value:
                cnt += 1

    return cnt


def bfs(visited, go):
    deq = deque()
    deq.append(go)

    visited[go[0]][go[1]] = 2

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    while deq:
        start_y, start_x = deq.popleft()

        for k in range(4):
            y = start_y + y_value[k]
            x = start_x + x_value[k]

            if 0 > y or y >= N or 0 > x or x >= M:
                continue

            if visited[y][x]:
                continue

            visited[y][x] = 2

            deq.append([y, x])


def set_wall(visited, wall):
    wall_one, wall_two, wall_three = wall

    wall_one_y = empty_space[wall_one][0]
    wall_one_x = empty_space[wall_one][1]

    visited[wall_one_y][wall_one_x] = 1

    wall_two_y = empty_space[wall_two][0]
    wall_two_x = empty_space[wall_two][1]

    visited[wall_two_y][wall_two_x] = 1

    wall_three_y = empty_space[wall_three][0]
    wall_three_x = empty_space[wall_three][1]

    visited[wall_three_y][wall_three_x] = 1


def get_combinations(cnt, cnt_limit, num, num_limit, combinations):
    if cnt == cnt_limit:
        wall_combinations.append(combinations[:])
        return

    for n in range(num, num_limit):
        combinations.append(n)
        get_combinations(cnt + 1, cnt_limit, n + 1, num_limit, combinations)
        combinations.pop()


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

virus = []
empty_space = []

wall_combinations = []

for i, row in enumerate(maps):
    for j, r in enumerate(row):
        if r == 2:
            virus.append([i, j])
        elif r == 0:
            empty_space.append([i, j])

# 벽을 세울 조합
# empty_space 의 인덱스 값으로 조합 구한다
# ex> [[0, 1, 2], ...]
get_combinations(0, 3, 0, len(empty_space), [])

answer = 0

for i, walls in enumerate(wall_combinations):
    copied_maps = copy.deepcopy(maps)

    set_wall(copied_maps, walls)

    for j, v in enumerate(virus):
        bfs(copied_maps, v)

    answer = max(answer, count_empty_spaces(copied_maps))

print(answer)

# 벽 조합 for loop
# -> maps 복사
# -> 벽 조합 하나 maps 배치
# -> virus for loop
# -> -> bfs
# -> 빈칸 세기
# -> 빈칸 최대값 비교

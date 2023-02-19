import copy


def get_combinations(cnt, cnt_limit, num, num_limit, combinations):
    if cnt == cnt_limit:
        wall_combinations.append(combinations[:])
        return

    for n in range(num, num_limit):
        combinations.append(n)
        get_combinations(cnt + 1, cnt_limit, n, num_limit, combinations)
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

get_combinations(0, 3, 0, len(empty_space), [])

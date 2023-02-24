from collections import deque


def move_population(q, avg):
    for idx, v in enumerate(q):
        population[v[0]][v[1]] = avg


def bfs(go, visited):
    deq = deque()
    deq.append(go)

    # 이번에 인구 이동할 나라만 모음
    # visited 와 구분 위함
    # 이미 인구 이동한 나라와
    # 이번에 인구 이동할 나라를 구분
    visited_today = [go]

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    sums = population[go[0]][go[1]]
    countries = 1

    while deq:
        y, x = deq.popleft()

        for i in range(4):
            y_idx = y + y_value[i]
            x_idx = x + x_value[i]

            # 땅 벗어 났는지
            if 0 > y_idx or y_idx >= N or 0 > x_idx or x_idx >= N:
                continue

            # 방문 여부
            if visited[y_idx][x_idx]:
                continue

            # 인구 차이
            population_diff = abs(population[y][x] - population[y_idx][x_idx])

            if L > population_diff or population_diff > R:
                continue

            deq.append([y_idx, x_idx])
            visited_today.append([y_idx, x_idx])
            visited[y_idx][x_idx] = True
            sums += population[y_idx][x_idx]
            countries += 1

    if countries > 1:
        move_population(visited_today, sums // countries)
        return True

    return False


def move():
    cnt = 0

    while True:
        visited = [[False] * N for _ in range(N)]

        bfs_cnt = 0

        for i, population_row in enumerate(population):
            for j, p in enumerate(population_row):
                if not visited[i][j]:
                    visited[i][j] = True

                    if bfs([i, j], visited):
                        bfs_cnt += 1

        if not bfs_cnt:
            break

        cnt += 1

    return cnt


N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]

print(move())

# visited, population
# 2개의 배열 준비
# visited 로 방문 체크
# while True 안에서
# population 을 for loop 돌면서
# 인구 이동이 가능한 지역 탐색 후 인구 이동 실시
# 인구 이동이 가능한 지역은 visited 에 체크
# 1일에 여러 지역 동시에 인구 이동이 발생 가능
# 하나의 for loop 가 1일을 의미 하는데
# 한 지역에 대해 인구 이동을 미리 시키면
# for loop 돌면서 이미 인구가 바뀌어 버려서
# 탐색에 영향을 주지 않도록 visited 를 함께 체크
#
# 방문만 한 지역과 인구 이동 하려는 지역을 어떻게 구분 지어야 할지
# -> 조건에 안 맞으면 방문 못 하므로 구분에 대해 고민할 필요 없다

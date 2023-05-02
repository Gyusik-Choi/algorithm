from collections import deque


def move_countries(move_info, num):
    for idx, move in enumerate(move_info):
        countries[move[0]][move[1]] = num


def bfs(go, visit):
    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    visit[go[0]][go[1]] = True
    sums = countries[go[0]][go[1]]
    cnt = 1
    move = [go]
    deq = deque()
    deq.append(go)

    while deq:
        y, x = deq.popleft()

        for k in range(4):
            y_idx, x_idx = y + y_value[k], x + x_value[k]

            if 0 > y_idx or y_idx >= N or 0 > x_idx or x_idx >= N:
                continue

            if visit[y_idx][x_idx]:
                continue

            if L > abs(countries[y][x] - countries[y_idx][x_idx]) or abs(countries[y][x] - countries[y_idx][x_idx]) > R:
                continue

            visit[y_idx][x_idx] = True
            sums += countries[y_idx][x_idx]
            cnt += 1
            move.append([y_idx, x_idx])
            deq.append([y_idx, x_idx])

    move_countries(move, sums // cnt)
    # cnt 를 리턴 하는데 기본 값이 1이라 if bfs([i, j], visited) 코드가 항상 참이 되므로
    # cnt - 1을 리턴 해서 한번도 이동이 없는 경우를 체크 한다
    return cnt - 1


N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

days = 0

while True:
    visited = [[False] * N for _ in range(N)]
    is_move = False

    for i, country_row in enumerate(countries):
        for j, c in enumerate(country_row):
            if visited[i][j]:
                continue

            if bfs([i, j], visited):
                is_move = True

    if not is_move:
        break

    days += 1

print(days)

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10
# => 3

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10
# => 2
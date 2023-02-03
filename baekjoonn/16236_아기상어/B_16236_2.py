import heapq
from collections import deque


def find_fish(start) -> list:
    heap = []

    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = True

    min_dist = 401

    deq = deque()
    start_distance = 0
    deq.append([start[0], start[1], start_distance])

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    while deq:
        y, x, distance = deq.popleft()
        # visited[y][x] = True

        if distance > min_dist:
            break

        for i in range(4):
            y_idx = y_direction[i] + y
            x_idx = x_direction[i] + x

            if 0 <= y_idx < N and 0 <= x_idx < N:
                if not visited[y_idx][x_idx] and sea[y_idx][x_idx] <= shark_size:
                    # 방문 처리를 deq 에서 꺼낼 때가 아니라
                    # 여기서 수행 하면서 시간 초과를 해결할 수 있었다
                    # 방문 처리를 보다 빨리 하면서 추가 탐색을 줄일 수 있었다
                    visited[y_idx][x_idx] = True

                    if 1 <= sea[y_idx][x_idx] < shark_size:
                        # distance + 1 이라고 생각 했는데
                        # distance 까지의 거리가 물고기를 찾을 수 있는 위치다
                        # 물고기 위치로 이동 하는게 distance + 1 이다
                        # 물고기 위치로 가지 않고 물고기를 찾을 수 있는 위치로
                        # min_dist 를 설정하면 물고기를 찾을 수 있는 지점까지만 탐색을 수행할 수 있다
                        # 물고기 위치로 가지 않아도 물고기를 찾을 수 있기 때문에
                        # 물고기를 찾을 수 있는 위치를 min_dist 로 설정하여 추가 탬색을 줄인다
                        min_dist = distance
                        heapq.heappush(heap, [distance + 1, y_idx, x_idx])
                    else:
                        if distance + 1 <= min_dist:
                            deq.append([y_idx, x_idx, distance + 1])

    if not heap:
        return []

    return heapq.heappop(heap)


def find_shark() -> list:
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                return [i, j]


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

shark_size = 2
shark_eat = 0

time = 0

while True:
    # 물고기 찾기 (상어 위치)
    shark = find_shark()
    fish = find_fish(shark)

    # 물고기 없으면 종료
    if not fish:
        break

    # 물고기 있으면 물고기 위치로 이동
    fish_dist, fish_y, fish_x = fish
    time += fish_dist
    sea[fish_y][fish_x] = 9

    # 기존 위치 초기화
    sea[shark[0]][shark[1]] = 0

    # shark_eat += 1
    shark_eat += 1

    # shark_size 비교
    if shark_eat == shark_size:
        shark_eat = 0
        shark_size += 1

print(time)

# 참고
# https://11001.tistory.com/96

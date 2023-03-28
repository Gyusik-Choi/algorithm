from collections import deque
import heapq


def move_shark():
    seconds = 0
    shark_size = 2
    shark_cnt = 0
    # 상어 위치 찾기
    # 물고기 탐색
    # 1) 가능한 물고기 없으면 종료
    # 2) 물고기 위치로 상어 이동
    # shark_cnt += 1
    # shark_size 올릴 수 있는지
    while True:
        shark = find_shark()
        fish = find_fish(shark, shark_size)

        if not fish:
            break

        dist, fish_y, fish_x = fish

        seconds += dist

        space[shark[0]][shark[1]] = 0
        space[fish_y][fish_x] = 9

        shark_cnt += 1

        if shark_cnt == shark_size:
            shark_size += 1
            shark_cnt = 0

    return seconds


def find_shark():
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                return [i, j]

    return []


def find_fish(shark, shark_size):
    heap = []

    deq = deque()
    deq.append([shark[0], shark[1], 0])

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    visited = [[False] * N for _ in range(N)]
    visited[shark[0]][shark[1]] = True

    while deq:
        y, x, dist = deq.popleft()

        # 여기서 heapq 에 넣을 물고기 찾지 않고
        # 아래 for 문을 돌면서 찾는다
        # if 0 < space[y][x] < shark_size:
            # heapq.heappush(heap, (dist, y, x))

        for i in range(4):
            y_idx, x_idx = y_value[i] + y, x_value[i] + x

            if 0 > y_idx or y_idx >= N or 0 > x_idx or x_idx >= N:
                continue

            if visited[y_idx][x_idx]:
                continue

            if space[y_idx][x_idx] > shark_size:
                continue

            visited[y_idx][x_idx] = True

            deq.append([y_idx, x_idx, dist + 1])

            if 0 < space[y_idx][x_idx] < shark_size:
                heapq.heappush(heap, (dist + 1, y_idx, x_idx))

    if heap:
        return heapq.heappop(heap)

    return heap


N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
print(move_shark())

from collections import deque
import heapq


def find_fish(space, shark) -> list:
    heap = []

    # 불필요한 추가 탐색을 막기 위한 변수
    # 최단 거리 물고기를 찾아야 해서
    # 아래 while 문 에서
    # min_dist 를 갱신 하고 min_dist 보다 먼 거리가 나오면 탐색 종료
    min_dist = len(space) * len(space)

    deq = deque()
    # 이동 거리, y, x
    deq.append([0, shark[0], shark[1]])

    visited = [[False] * len(space) for _ in range(len(space))]
    visited[shark[0]][shark[1]] = True

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    while deq:
        dist, y, x = deq.popleft()

        if min_dist < dist:
            break

        for i in range(4):
            y_idx, x_idx = y + y_value[i], x + x_value[i]

            if 0 > y_idx or y_idx >= len(space) or 0 > x_idx or x_idx >= len(space):
                continue

            if visited[y_idx][x_idx]:
                continue

            visited[y_idx][x_idx] = True

            if not space[y_idx][x_idx]:
                deq.append([dist + 1, y_idx, x_idx])

            if 1 <= space[y_idx][x_idx] <= 6 and space[y_idx][x_idx] <= shark_size:
                deq.append([dist + 1, y_idx, x_idx])

                if space[y_idx][x_idx] < shark_size:
                    min_dist = dist + 1
                    heapq.heappush(heap, [dist + 1, y_idx, x_idx])

    if not heap:
        return [0, -1, -1]

    return heapq.heappop(heap)


def find_shark(space) -> list:
    for i in range(len(space)):
        for j in range(len(space)):
            if space[i][j] == 9:
                return [i, j]

    return []


def leave_shark(space, shark):
    space[shark[0]][shark[1]] = 0


def move_shark_to_fish(space, shark):
    space[shark[0]][shark[1]] = 9


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2
shark_cnt = 0
answer = 0

while True:
    # 상어 위치
    cur_shark = find_shark(sea)
    # 물고기 위치
    time, new_shark_y, new_shark_x = find_fish(sea, cur_shark)

    if not time:
        break

    # 기존 상어 위치 빈칸
    leave_shark(sea, cur_shark)
    # 상어 이동
    move_shark_to_fish(sea, [new_shark_y, new_shark_x])
    answer += time
    shark_cnt += 1

    if shark_cnt == shark_size:
        shark_size += 1
        shark_cnt = 0

print(answer)

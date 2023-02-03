from collections import deque
import heapq


def bfs(shark_y_idx, shark_x_idx):
    deq = deque()
    deq.append([0, shark_y_idx, shark_x_idx])

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    min_dist = 401
    visited = [[False] * N for _ in range(N)]
    visited[shark_y_idx][shark_x_idx] = True
    heap = []

    while deq:
        dist, y_idx, x_idx = deq.popleft()

        if dist > min_dist:
            break

        for k in range(4):
            y = y_direction[k] + y_idx
            x = x_direction[k] + x_idx

            if 0 <= y < N and 0 <= x < N:
                # 방문 안했고 상어 크기보다 크거나 같은 지점
                # 케이스 3개 => 0, shark_size 보다 작은 지점, shark_size 와 같은 지점
                if not visited[y][x] and sea[y][x] <= shark_size:
                    visited[y][x] = True

                    # 먹을 수 있는 물고기가 있으면
                    # 여기보다 더 멀리있는 물고기를 찾을 필요가 없어서
                    # 큐에 담지 않는다
                    if 0 < sea[y][x] < shark_size:
                        min_dist = dist
                        heapq.heappush(heap, [dist + 1, y, x])
                    else:
                        # 0 혹은 shark_size 와 같은 크기의 물고기면서
                        # 해당 지점에서 한칸씩 더 가도 최소 거리 보다 작거나 같을 경우
                        # 추가적으로 탐색할 수 있다
                        if dist + 1 <= min_dist:
                            deq.append([dist + 1, y, x])

    if heap:
        distance, y_axis, x_axis = heapq.heappop(heap)
        return [distance, y_axis, x_axis]
    else:
        return False


def find_shark():
    shark_y_idx = -1
    shark_x_idx = -1

    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                shark_y_idx = i
                shark_x_idx = j
                sea[i][j] = 0

    return [shark_y_idx, shark_x_idx]


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
shark_y, shark_x = find_shark()
shark_size = 2
fish = 0
time = 0

while True:
    bfs_result = bfs(shark_y, shark_x)
    if not bfs_result:
        break

    min_distance, y_info, x_info = bfs_result
    time += min_distance
    shark_y = y_info
    shark_x = x_info
    sea[shark_y][shark_x] = 0

    fish += 1
    if fish == shark_size:
        fish = 0
        shark_size += 1

print(time)

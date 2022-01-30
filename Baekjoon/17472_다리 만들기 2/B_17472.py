from collections import deque
import heapq


def is_all_true():
    for m in range(1, len(mst)):
        if not mst[m]:
            return False

    return True


# 섬 간선
def get_edges(c):
    deq = deque()

    y, x, marking_num = c
    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    for k in range(4):
        deq.append([y, x])
        visited = [[False] * M for _ in range(N)]
        visited[y][x] = True
        visited_distance = [[0] * M for _ in range(N)]

        while deq:
            y_start, x_start = deq.popleft()

            y_idx = y_start + y_direction[k]
            x_idx = x_start + x_direction[k]

            if 0 <= y_idx < N and 0 <= x_idx < M:
                if not visited[y_idx][x_idx]:
                    visited[y_idx][x_idx] = True

                    if numbered_islands[y_idx][x_idx] == 0:
                        visited_distance[y_idx][x_idx] = visited_distance[y_start][x_start] + 1
                        deq.append([y_idx, x_idx])
                    elif numbered_islands[y_idx][x_idx] != marking_num and visited_distance[y_start][x_start] >= 2:
                        # 시작점, 도착점, 거리
                        edges.append([marking_num, numbered_islands[y_idx][x_idx], visited_distance[y_start][x_start]])


# 섬 번호 마킹
def dfs_recursion(y, x, marking_number, marking_islands):
    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    for k in range(4):
        y_idx = y + y_direction[k]
        x_idx = x + x_direction[k]

        if 0 <= y_idx < N and 0 <= x_idx < M:
            if not marking_islands[y_idx][x_idx] and islands[y_idx][x_idx]:
                marking_islands[y_idx][x_idx] = marking_number
                # 섬의 좌표 => [y축, x축, 섬 번호]
                coordinates.append([y_idx, x_idx, marking_number])
                dfs_recursion(y_idx, x_idx, marking_number, marking_islands)

    return marking_islands


N, M = map(int, input().split())
islands = [list(map(int, input().split())) for _ in range(N)]
# 섬 번호를 포함한 좌표(dfs_recursion 함수에서 구해진다)
coordinates = []

number = 1
numbered_islands = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        num = islands[i][j]

        if num and not numbered_islands[i][j]:
            numbered_islands[i][j] = number
            coordinates.append([i, j, number])
            numbered_islands = dfs_recursion(i, j, number, numbered_islands)
            number += 1

edges = []

for i, coordinate in enumerate(coordinates):
    get_edges(coordinate)
edges_dict = {i: [] for i in range(1, number)}

for edge in edges:
    s, e, v = edge
    edges_dict[s].append([e, v])
    edges_dict[e].append([s, v])

INF = float('inf')
mst = [False] * number
key = [INF] * number

# 1번 섬을 시작점으로 지정
key[1] = 0
heap = [(0, 1)]

answer = 0
while heap:
    value, start = heapq.heappop(heap)

    if not mst[start]:
        mst[start] = True
        answer += value

        if edges_dict[start]:
            for end, val in edges_dict[start]:
                if not mst[end] and key[end] > val:
                    key[end] = val
                    heapq.heappush(heap, (val, end))

if not is_all_true():
    print(-1)
else:
    print(answer)

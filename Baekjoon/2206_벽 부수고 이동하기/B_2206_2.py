from collections import deque
import sys


def check_breaking(y, x):
    visited[y][x][1] = 1
    return


def check_visit(y, x):
    visited[y][x][0] = 1
    return


def bfs(y, x, c):
    deq = deque()
    deq.append([y, x, c])
    y_location = [-1, 0, 1, 0]
    x_location = [0, 1, 0, -1]
    while deq:
        popped_y, popped_x, cnt = deq.popleft()
        for i in range(4):
            y_idx = popped_y + y_location[i]
            x_idx = popped_x + x_location[i]
            if 0 <= y_idx < N and 0 <= x_idx < M:
                if y_idx == N - 1 and x_idx == M - 1:
                    cnt += 1
                    return cnt

                visit = visited[y_idx][x_idx][0]
                breaking = visited[y_idx][x_idx][1]
                if not visit:
                    # 0일 경우
                    if not maps[y_idx][x_idx]:
                        cnt += 1
                        deq.append([y_idx, x_idx, cnt])
                        check_visit(y_idx, x_idx)
                    # 1일 경우
                    else:
                        # 부순적 X
                        if not breaking:
                            cnt += 1
                            deq.append([y_idx, x_idx, cnt])
                            check_visit(y_idx, x_idx)
                            check_breaking(y_idx, x_idx)
    cnt = -1
    return cnt


N, M = map(int, sys.stdin.readline().split())
maps = []
for _ in range(N):
    temp_map = list(map(int, sys.stdin.readline().strip()))
    maps.append(temp_map)

# 부수고 가는 경우와 안 부수고 가는 경우를 모두 고려해야함
# 1을 만났을때, 부순적이 이전에 있으면 부술 수 없어서 지나쳐야 하고
# 부순적이 없으면 부수고 갈 수도 있고 그냥 지나칠 수도 있다

# 방문, 부쉈는지
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
answer = bfs(0, 0, 1)
print(answer)

# 현재 의문사항...
# 전역에 방문체크를 두면 이후에 최단으로 갈수있는 노드가
# 이전에 최단으로 갈 수 없는 노드가 이미 거쳐갔다는 이유로 방문을 못하게 되지 않는지...

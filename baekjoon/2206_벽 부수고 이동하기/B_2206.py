from collections import deque


def bfs(deq):
    # 상 우 하 좌
    y_axis = [-1, 0, 1, 0]
    x_axis = [0, 1, 0, -1]
    while deq:
        y, x, is_break = deq.popleft()
        if y == N - 1 and x == M - 1:
            return visited[y][x][is_break]
        for j in range(4):
            y_idx = y + y_axis[j]
            x_idx = x + x_axis[j]
            if 0 <= y_idx < N and 0 <= x_idx < M:
                if maps[y_idx][x_idx] == 0 and visited[y_idx][x_idx][is_break] == 0:
                    visited[y_idx][x_idx][is_break] = visited[y][x][is_break] + 1
                    deq.append([y_idx, x_idx, is_break])
                elif maps[y_idx][x_idx] == 1 and is_break == 0:
                    visited[y_idx][x_idx][is_break + 1] = visited[y][x][is_break] + 1
                    deq.append([y_idx, x_idx, is_break + 1])
    return -1


N, M = map(int, input().split())
maps = []
for i in range(N):
    nums = list(map(int, input()))
    maps.append(nums)

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

d = deque()
d.append([0, 0, 0])
ans = bfs(d)
print(ans)

# 참고
# https://tmdrl5779.tistory.com/15
# https://www.acmicpc.net/board/view/69214
# https://www.acmicpc.net/board/view/66299

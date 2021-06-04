from collections import deque


def bfs(deq):
    y_axis = [1, 0, -1, 0]
    x_axis = [0, 1, 0, -1]

    while deq:
        item = deq.popleft()
        y_location = item[0]
        x_location = item[1]

        for k in range(4):
            y_idx = y_axis[k] + y_location
            x_idx = x_axis[k] + x_location
            if 0 <= y_idx < N and 0 <= x_idx < M:
                if boxes[y_idx][x_idx] == 0:
                    boxes[y_idx][x_idx] = boxes[y_location][x_location] + 1
                    deq.append([y_idx, x_idx])

    ans = -1
    for box in boxes:
        for tomato in box:
            if tomato == 0:
                return -1
            ans = max(ans, tomato)
    return ans - 1


M, N = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]

d = deque()
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 1:
            d.append([i, j])

days = bfs(d)
print(days)

# 참고
# https://hwiyong.tistory.com/389
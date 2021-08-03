import sys
from collections import deque


def bfs(y, x, cnt):
    global visited
    deq = deque()
    deq.append([y, x, cnt])
    y_location = [-1, 0, 1, 0]
    x_location = [0, 1, 0, -1]
    while deq:
        y_idx, x_idx, move = deq.popleft()
        for i in range(4):
            y_coordinate = y_location[i] + y_idx
            x_coordinate = x_location[i] + x_idx
            if y_coordinate == N - 1 and x_coordinate == M - 1:
                return move + 1
            if 0 <= y_coordinate < N and 0 <= x_coordinate < M and maze[y_coordinate][x_coordinate]:
                if not visited[y_coordinate][x_coordinate] and [y_coordinate, x_coordinate, move + 1] not in deq:
                    visited[y_coordinate][x_coordinate] = 1
                    deq.append([y_coordinate, x_coordinate, move + 1])


N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze_info = list(map(int, sys.stdin.readline().rstrip()))
    maze.append(maze_info)

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
answer = bfs(0, 0, 1)
sys.stdout.write(str(answer))

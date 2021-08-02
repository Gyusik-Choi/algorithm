import sys
import copy
sys.setrecursionlimit(2600)


# vertical, horizontal
def dfs_recursion(v, h):
    global visited
    visited[v][h] = 1
    v_location = [-1, 0, 1, 0]
    h_location = [0, 1, 0, -1]
    for k in range(4):
        v_idx = v_location[k] + v
        h_idx = h_location[k] + h
        if 0 <= v_idx < N and 0 <= h_idx < M:
            if field[v_idx][h_idx] and not visited[v_idx][h_idx]:
                dfs_recursion(v_idx, h_idx)
    return


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    # 가로, 세로, 배추 갯수
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * M for _ in range(N)]
    visited = copy.deepcopy(field)
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] and not visited[i][j]:
                dfs_recursion(i, j)
                cnt += 1

    sys.stdout.write(str(cnt) + "\n")

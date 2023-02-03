import sys


def dfs_recursion(y, x):
    global visited, cnt
    y_axis = [-1, 0, 1, 0]
    x_axis = [0, 1, 0, -1]
    for k in range(4):
        y_index = y_axis[k] + y
        x_index = x_axis[k] + x
        if 0 <= y_index < N and 0 <= x_index < N:
            if visited[y_index][x_index] == 0 and apartments[y_index][x_index] == 1:
                visited[y_index][x_index] = 1
                dfs_recursion(y_index, x_index)
                cnt += 1
    return


N = int(sys.stdin.readline())
apartments = []
for _ in range(N):
    # apartment = list(map(int, input()))
    apartment = list(map(int, sys.stdin.readline().rstrip()))
    apartments.append(apartment)

answer = []
cnt = 1
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if apartments[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            dfs_recursion(i, j)
            answer.append(cnt)
            cnt = 1

answer.sort()
sys.stdout.write(str(len(answer)) + "\n")
for a in answer:
    sys.stdout.write(str(a) + "\n")

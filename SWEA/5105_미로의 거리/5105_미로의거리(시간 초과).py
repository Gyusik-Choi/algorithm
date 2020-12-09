def bfs(departure):
    lst = [[0] * N for _ in range(N)]
    ay = [1, -1, 0, 0]
    ax = [0, 0, -1, 1]
    depart = [departure]
    visit = []
    while depart:
        go = depart.pop(0)
        visit.append(go)
        y = go[0]
        x = go[1]
        for k in range(4):
            dy = y + ay[k]
            dx = x + ax[k]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] == 3:
                    return lst[y][x]
                elif arr[dy][dx] == 0 and [dy, dx] not in depart and [dy, dx] not in visit:
                    depart.append([dy, dx])
                    lst[dy][dx] = lst[y][x] + 1

    return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                start.extend([i, j])
                break
    ans = bfs(start)
    print("#{} {}".format(t, ans))
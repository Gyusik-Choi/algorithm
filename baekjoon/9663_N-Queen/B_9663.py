def n_queen(y):
    global cnt
    if y == N:
        cnt += 1
        return
    else:
        for x in range(N):
            if not vertical[x] and not diagonal1[N - (y - x) - 1] and not diagonal2[y + x]:
                vertical[x] = 1
                diagonal1[N - (y - x) - 1] = 1
                diagonal2[y + x] = 1
                n_queen(y + 1)
                vertical[x] = 0
                diagonal1[N - (y - x) - 1] = 0
                diagonal2[y + x] = 0


N = int(input())
vertical = [0] * N
diagonal1 = [0] * (2*N - 1)
diagonal2 = [0] * (2*N - 1)
cnt = 0
n_queen(0)
print(cnt)

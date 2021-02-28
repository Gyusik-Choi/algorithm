def check(x):
    for y in range(x):
        if row[x] == row[y]:
            return False
        if abs(row[x] - row[y]) == x - y:
            return False
    return True


def n_queen(x):
    global cnt
    if x == N:
        cnt += 1
    else:
        for y in range(N):
            row[x] = y
            if check(x):
                n_queen(x + 1)


N = 4
row = [0] * N
cnt = 0
n_queen(0)
print(cnt)

# row 는 가로(x축)
# row 값을 0부터 N-1 까지 올려가는데 이게 세로(y축)

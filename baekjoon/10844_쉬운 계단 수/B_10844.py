N = int(input())
arr = [[0] * 10 for _ in range(N)]
for i in range(1, 10):
    arr[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j - 1 >= 0:
            arr[i][j] += arr[i - 1][j - 1]

        if j + 1 <= 9:
            arr[i][j] += arr[i - 1][j + 1]

sums = 0
for i in range(10):
    sums += arr[N - 1][i]

print(sums % 1000000000)

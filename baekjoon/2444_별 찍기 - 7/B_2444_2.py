N = int(input())
for i in range(1, 2 * N):
    if i > 2 * N // 2:
        i = N - (i - N)
    print(' ' * (N - i) + '*' * (2 * i - 1))

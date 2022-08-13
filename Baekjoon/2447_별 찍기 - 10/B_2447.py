import sys


def recursion(n, y, x):
    if n == 1:
        stars[y][x] = '*'
        return

    n //= 3

    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                recursion(n, n * i + y, n * j + x)


N = int(input())
stars = [[' '] * N for _ in range(N)]
recursion(N, 0, 0)
for star in stars:
    sys.stdout.write(''.join(star) + "\n")

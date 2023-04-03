import sys


N = int(input())

for i in range(1, 2 * N):
    if i > 2 * N // 2:
        i = N - (i - N)

    for j in range(N - i):
        sys.stdout.write(" ")

    for j in range(2 * i - 1):
        sys.stdout.write("*")

    sys.stdout.write("\n")

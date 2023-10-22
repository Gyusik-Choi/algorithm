import sys


m, n = map(int, input().strip().split(' '))
for i in range(n):
    for j in range(m):
        sys.stdout.write("*")
    sys.stdout.write("\n")

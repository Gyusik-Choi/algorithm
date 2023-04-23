import sys


N = int(sys.stdin.readline())

max_y = -10000
max_x = -10000
min_y = 10000
min_x = 10000

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    max_y = max(max_y, a)
    max_x = max(max_x, b)
    min_y = min(min_y, a)
    min_x = min(min_x, b)

sys.stdout.write(str(abs(max_y - min_y) * abs(max_x - min_x)))

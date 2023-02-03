import sys


N = int(sys.stdin.readline())
grades = [list(sys.stdin.readline().split()) for _ in range(N)]
grades.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for idx, value in enumerate(grades):
    sys.stdout.write(value[0] + "\n")

import sys


N = int(input())
arr = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort(key=lambda a: (a[1], a[0]))
for idx, num in enumerate(arr):
    num = map(str, num)
    sys.stdout.write(' '.join(num) + "\n")

import sys


N = int(input())
arr = [0] * 10001
for i in range(N):
    number = int(sys.stdin.readline())
    arr[number] += 1

for idx, num in enumerate(arr):
    if num != 0:
        for j in range(num):
            sys.stdout.write(str(idx) + '\n')
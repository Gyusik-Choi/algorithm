from bisect import bisect_left
import sys


N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))

lis = [numbers[0]]
for idx, value in enumerate(numbers):
    if idx > 0:
        if value > lis[-1]:
            lis.append(value)
        else:
            if value < lis[-1]:
                idx = bisect_left(lis, value)
                lis[idx] = value

sys.stdout.write(str(len(lis)))

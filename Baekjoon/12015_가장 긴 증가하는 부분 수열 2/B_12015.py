import sys


def binary_search(start, end, target):
    if start >= end:
        return end

    mid = (start + end) // 2
    if lis[mid] > target:
        return binary_search(start, mid, target)
    else:
        if lis[mid] == target:
            return mid
        return binary_search(mid + 1, end, target)


N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))

lis = [numbers[0]]
for idx, value in enumerate(numbers):
    if idx > 0:
        if value > lis[-1]:
            lis.append(value)
        else:
            if value < lis[-1]:
                idx = binary_search(0, len(lis) - 1, value)
                lis[idx] = value

sys.stdout.write(str(len(lis)))

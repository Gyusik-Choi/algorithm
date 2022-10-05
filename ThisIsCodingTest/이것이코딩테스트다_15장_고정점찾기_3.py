import sys


def binary_search(start, end):
    if start >= end:
        if numbers[end] == end:
            return end

        return -1

    mid = (start + end) // 2

    if numbers[mid] == mid:
        return mid

    if numbers[mid] > mid:
        return binary_search(start, mid - 1)

    return binary_search(mid + 1, end)


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
print(binary_search(0, N - 1))

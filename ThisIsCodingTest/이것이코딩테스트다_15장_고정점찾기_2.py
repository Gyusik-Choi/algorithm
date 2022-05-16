import sys


def binary_search(start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if numbers[mid] == mid:
        return mid
    elif numbers[mid] > mid:
        return binary_search(start, mid - 1)
    else:
        return binary_search(mid + 1, end)


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
if numbers[0] == 0:
    sys.stdout.write(str(0))
elif numbers[N - 1] == N - 1:
    sys.stdout.write(str(N - 1))
else:
    answer = binary_search(0, N - 1)
    if answer == -1:
        print(-1)
    else:
        print(answer)

# 5
# -15 -6 1 3 7
# => 3

# 7
# -15 -4 2 8 9 13 15
# => 2

# 7
# -15 -4 3 8 9 13 15
# => -1

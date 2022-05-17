import sys


def get_max_distance(limit):
    start = 0
    end = 1

    cnt = 1

    while end < N:
        if houses[end] - houses[start] > limit:
            start += 1
            end += 1
            cnt += 1
        else:
            end += 1

    return cnt


def binary_search(start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if get_max_distance(mid) >= C:
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid)




N, C = map(int, sys.stdin.readline().split())
houses = []
for _ in range(N):
    house = int(sys.stdin.readline())
    houses.append(house)

houses.sort()

binary_search(0, N - 1)

# https://st-lab.tistory.com/277

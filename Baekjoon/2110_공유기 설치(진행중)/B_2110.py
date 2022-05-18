import sys


def get_max_distance(limit):
    start = houses[0]
    cnt = 1

    for i in range(1, N):
        if houses[i] - start >= limit:
            cnt += 1
            start = houses[i]

    return cnt


def binary_search(start, end):
    global answer
    if start > end:
        return

    mid = (start + end) // 2
    cnt = get_max_distance(mid)

    if cnt >= C:
        answer = mid
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)


N, C = map(int, sys.stdin.readline().split())
houses = []
for _ in range(N):
    house = int(sys.stdin.readline())
    houses.append(house)

houses.sort()

answer = 1

# 최소 거리, 최대 거리
binary_search(1, houses[-1] - houses[0])

print(answer)

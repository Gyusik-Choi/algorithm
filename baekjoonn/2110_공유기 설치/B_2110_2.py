import sys


def get_router_count(distance):
    cnt = 1
    last_house = houses[0]

    for i in range(1, N):
        current_house = houses[i]

        if current_house - last_house >= distance:
            cnt += 1
            last_house = current_house

    return cnt


def binary_search(start, end):
    global answer

    while start <= end:
        mid = (start + end) // 2

        if get_router_count(mid) >= C:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1


N, C = map(int, sys.stdin.readline().split())
houses = sorted([int(sys.stdin.readline()) for _ in range(N)])

answer = 1
binary_search(1, houses[-1] - houses[0])
print(answer)

import sys


def binary_search(start, end):
    global ans
    if start > end:
        return

    mid = (start + end) // 2
    cnt = 1
    first_home = coordinates[0]
    for i in range(1, N):
        if coordinates[i] - first_home >= mid:
            first_home = coordinates[i]
            cnt += 1

    if cnt >= C:
        ans = mid
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)


N, C = map(int, sys.stdin.readline().split())
coordinates = []
for _ in range(N):
    coordinate = int(sys.stdin.readline().rstrip())
    coordinates.append(coordinate)

coordinates.sort()

minimum = 1
maximum = coordinates[-1] - coordinates[0]

ans = 0
binary_search(minimum, maximum)
sys.stdout.write(str(ans))

# 참고
# https://jaimemin.tistory.com/966

# 8 4
# 1
# 3
# 6
# 11
# 13
# 17
# 25
# 29

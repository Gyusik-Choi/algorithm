import sys


def possible_router(home, distance):
    router = 1
    start = home[0]

    for i in range(1, len(home)):
        end = home[i]

        if end - start >= distance:
            router += 1
            start = end

    return router


def binary_search(home, router):
    global max_distance

    # bisect 모듈의 bisect_right 를 참고해서
    # high 를 최대 거리 + 1 로 설정했다
    # 만약에 high 가 home[-1] - home[0] 이면
    # while 문의 low < high 조건에 걸려서
    # home[-1] - home[0] 거리 값은 possible_router 로 탐색할 수 없다
    # low 가 1 이라 while 문 조건에 맞춘 가장 큰 거리는
    # home[-1] - home[0] - 1 이다
    low, high = 1, home[-1] - home[0] + 1

    while low < high:
        mid = (low + high) // 2

        if possible_router(home, mid) >= router:
            max_distance = max(max_distance, mid)
            low = mid + 1
        else:
            high = mid

    return low


N, C = map(int, sys.stdin.readline().split())
house = []

for _ in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()
max_distance = 0
binary_search(house, C)
print(max_distance)

# 집 사이의 거리로 이진 탐색
# 거리를 기준으로
# 설치 하려는 공유기 숫자가
# C 보다 많으면 거리를 늘리고
# C 보다 작으면 거리를 줄인다
# C 랑 같으면 거리를 늘린다

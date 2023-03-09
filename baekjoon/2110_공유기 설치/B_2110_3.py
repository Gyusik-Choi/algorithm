import sys


def get_count(distance):
    cnt = 1
    prev = houses[0]

    for i in range(1, len(houses)):
        cur = houses[i]

        if cur - prev >= distance:
            prev = cur
            cnt += 1

    return cnt



def binary_search(low, high):
    answer = 1

    # low < high 가 아닌 low <= high 다
    # 앞선 이진 탐색 문제들 풀이시
    # low < high 조건에 low 값을 리턴 하는 방식을 활용 했는데
    # 이번 풀이는 다르게 진행 한다
    # 우선 리턴 하는 값이 low 가 아니다
    # mid 값으로 answer 를 갱신 해서
    # low < high 라면 low <= high 인 상황은
    # 값을 갱신 못한다
    # low < high 조건에 low 값을 리턴 하는 방식일 경우는
    # low >= high 일때 while 문이 끝나고 low 를 리턴 하므로
    # low 나 high 가 갱신 되면서 low >= high 로 넘어 오는데
    # 이 경우는 답으로 리턴할 answer 는 mid 값에 의존 한다
    # mid 값은 while 문 안의 else 문에서 갱신 된다
    # 만약에 low 를 리턴 한다면 low >= high 조건이 될 때
    # low 가 갱신된 채로 넘어 오는데 반해
    # mid 값을 리턴 하는 경우면 low < high 의 경우만
    # mid 값이 갱신 되고
    # low >= high 조건이 될 때는
    # while 문을 돌지 않아서 mid 값이 갱신 되지 못한다
    while low <= high:
        mid = (low + high) // 2

        if get_count(mid) < C:
            # while 문의 조건이 low <= high 라서
            # high = mid 일 경우
            # 무한 루프를 돌 수도 있어서
            # mid - 1 로 설정 한다
            high = mid - 1
        else:
            answer = mid
            low = mid + 1

    return answer


N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

# 집의 개수가 최소 2개, 한 집에는 공유기 하나만 설치 가능 하므로 최소 거리는 1 이 된다
start = 1
end = houses[-1] - houses[0]

print(binary_search(start, end))

# 3 2
# 1
# 100
# 1000
# => 999

# 3 2
# 1
# 5
# 10
# => 9

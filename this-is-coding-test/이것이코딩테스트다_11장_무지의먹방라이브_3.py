from collections import deque


def solution(food_times, k):
    # k 초 후에 먹을 음식이 더 없을 경우
    if k >= sum(food_times):
        return -1

    # 음식 시간, 인덱스
    q = []

    for idx, time in enumerate(food_times):
        q.append([time, idx])

    # 정렬 후 데크에 담는다
    sorted_food_times = deque(sorted(q, key=lambda x: x[0]))

    # 음식 길이
    food_length = len(food_times)

    # 이전 음식 시간
    previous_time = 0

    # 음식 길이 * (현재 먹을 음식 시간 - 이전 음식 시간) < k
    # 이전 음식 시간을 뺀 현재 음식 시간을 남은 음식 길이 만큼 다 먹어도 k 보다 큰지
    # 최소 한 사이클 만큼 다 먹을 수 있는지
    while food_length * (sorted_food_times[0][0] - previous_time) < k:
        # 음식 시간, 인덱스
        time, idx = sorted_food_times.popleft()

        k -= (time - previous_time) * food_length

        # 이전 음식 시간을 현재 음식 시간 설정
        previous_time = time

        food_length -= 1

    # 인덱스 순서로 재정렬
    resorted_food_times = sorted(list(sorted_food_times), key=lambda x: x[1])
    # k 가 몇 인지 중요 하지만 단순히 k 값의 인덱스 구하면 안 된다
    # 이미 다 먹은 음식의 갯수는 제외 하고 인덱스 구해야 한다
    # food_length 가 k 보다 클 수 있어서 k % food_length 로 인덱스 구한다
    # 그렇게 구한 값에서 1 인덱스 값이 해당 음식의 인덱스 값이다
    # 여기서 1을 더해야 몇 번째 음식에 해당 되는지 알 수 있음
    return resorted_food_times[k % food_length][1] + 1


print(solution([3, 1, 2], 5))

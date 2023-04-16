from collections import deque


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food = list()

    for i, t in enumerate(food_times):
        food.append([i + 1, t])

    food = deque(sorted(food, key=lambda x: x[1]))

    food_length = len(food)
    previous_time = 0

    while (food[0][1] - previous_time) * food_length < k:
        idx, time = food.popleft()
        k -= (time - previous_time) * food_length
        # 왜 previous_time += time 이 아니고 previous_time = time 인지 이해 하는데 오래 걸렸다
        # food_times 가 [1, 2, 5] 인 상황을 예로 들어 보자
        # previous_time 은 처음에 1이 되고 그 다음은 3이 아닌 2가 되어야 한다
        # previous_time 이 1이 될때 한 사이클 돈다
        # 그러면 1만 0이 되는게 아니라 2도 1이 줄어서 1이 된다 (물론 5도 4가 된다)
        # previous_time 이 1이 되고 그 다음 while 문을 볼때
        # food_times 는 [0, 1, 4] 인 상황이 됐다
        # 기존에 2였던 값은 1만 남았다
        # 이렇게 food_times 값을 사이클 돌면서 모두 줄여 준다면
        # previous_time += time 이 가능 한데
        # 이 풀이는 그렇게 진행 하지 않는다
        # food_times 값을 모두 줄이지 않고 food_times 에서 popleft 를 통해 하나씩 제거해 나간다
        # 그래서 food_times 에 남은 값은 값이 줄지 않고 원래 값은 유지 하므로
        # previous_time = time 이 되어야 한다
        previous_time = time
        food_length -= 1

    food = sorted(food, key=lambda x: x[0])
    # k 에서 food_length 를 나눈 값을 구하는 이유를 한참 동안 이해 못했다
    # 한 사이클 돌 수 없어서 while 문을 나왔다
    # 주의할 점은 먹어야 할 음식 총 시간 값이 k 보다는 크지만
    # 음식 길이가 k 보다는 짧을 수 있다
    # while 문의 조건은 음식 길이만 k 와 비교 하는게 아니다
    # (현재 음식 시간 - 이전 음식 시간) * 음식 길이를 k 와 비교 한다
    # 아래는 음식 길이만 본다
    # 예를 들어 food[0][1] - previous_time 이 5, food_length 가 1, k 가 2라면
    # while 문을 빠져 나온다
    # 이때 food_length 보다 k 가 더 크다
    return food[k % food_length][0]


print(solution([3, 1, 2], 5))
print(solution([3, 4, 1, 2], 5))

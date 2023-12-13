from collections import deque
from math import ceil


def solution(progresses, speeds):
    complete = 100
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []

    while progresses:
        work_days = ceil((complete - progresses[0]) / speeds[0])

        for idx, value in enumerate(progresses):
            progresses[idx] += work_days * speeds[idx]

        cnt = 0

        for _ in range(len(progresses)):
            if progresses[0] >= complete:
                progresses.popleft()
                speeds.popleft()
                cnt += 1

        answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# // 연산자를 사용할 경우 몫만 나오기 때문에
# 실제로 작업해야 할 날보다 하루 적게 나올 수 있다
# 예를 들어 남은 작업량 보다 속도가 더 커서 work_days 가 0이 나올 수 있다
# 예를 들어 진도가 92, 속도가 5일 때
# // 연산자를 사용해서 work_days 를 구하면 1이 된다
# 실제로는 1일이 아니라 2일이 필요하다
print(solution([50, 50, 50, 20], [50, 50, 50, 50]))
print(solution([30, 30, 30, 10, 2], [5, 5, 5, 5, 5]))

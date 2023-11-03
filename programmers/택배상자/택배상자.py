# 컨테이너 벨트에 상자 1 ~ n 순서 -> 1번 상자부터 내릴 수 있음
#
# 컨테이너 벨트 -> queue
# 보조 컨테이너 벨트 -> stack
from collections import deque


def solution(order):
    length = len(order)
    container = deque([box for box in range(1, length + 1)])
    sub_container = []
    cnt = 0

    for box in order:
        if container and container[0] == box:
            cnt += 1
            container.popleft()
            continue

        if sub_container and sub_container[-1] == box:
            cnt += 1
            sub_container.pop()
            continue

        while container:
            if container[0] > box:
                return cnt

            if container[0] == box:
                container.popleft()
                cnt += 1
                break

            sub_container.append(container.popleft())

    return cnt


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))

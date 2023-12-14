from collections import deque


def get_max_priority(priorities):
    max_priority = 0

    for idx, priority in priorities:
        max_priority = max(max_priority, priority)

    return max_priority


def solution(priorities, location):
    priorities = deque([idx, priority] for idx, priority in enumerate(priorities))
    max_priority = get_max_priority(priorities)
    order = 0

    while priorities:
        i, p = priorities.popleft()

        # 대상 프로세스
        if i == location:
            # 가장 높은 우선 순위일 경우
            if p == max_priority:
                # 실행 시키고 종료
                order += 1
                break
            # 가장 높은 우선 순위가 아닐 경우
            else:
                # 꺼낸 프로세스를 다시 큐에 넣는다
                priorities.append([i, p])
        # 대상 프로세스 아닐 때
        else:
            # 가장 높은 우선 순위일 경우
            if p == max_priority:
                # 실행 시키고 우선 순위 갱신
                order += 1
                max_priority = get_max_priority(priorities)
            # 가장 높은 우선 순위가 아닐 경우
            else:
                # 꺼낸 프로세스를 다시 큐에 넣는다
                priorities.append([i, p])

    return order


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

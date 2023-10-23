# !!!
# num_courses 가 5 라고 해서
# 0 ~ 4까지 모든 숫자가 course 로 주어지지 않을 수 있다는 점에 주의해야 한다
# !!!
from collections import defaultdict, deque


# 1 이상인게 있는데 탐색이 끝남
def is_cycle(exist, degree) -> bool:
    for i in range(len(degree)):
        if exist[i] and degree[i]:
            return True

    return False


def find_starts(exist, degree) -> list:
    starts = []

    for i in range(len(degree)):
        if exist[i] and not degree[i]:
            starts.append(i)

    return starts


def topology_sort(courses, requisites):
    if not requisites:
        return True

    # 0부터 courses - 1 까지
    # 모든 숫자가 pre_requisites 정보로 주어지지 않을 수 있다
    # 출발점을 찾거나 사이클이 있는지 판별할 때
    # 존재하지 않는 정점을 포함하지 않도록
    # is_exist 리스트로 검사한다
    is_exist = [False] * courses
    in_degree = [0] * courses
    adj = defaultdict(list)

    for req in requisites:
        first, second = req
        is_exist[first] = is_exist[second] = True
        in_degree[second] += 1
        adj[first].append(second)

    starts = find_starts(is_exist, in_degree)

    if not starts:
        return False

    deq = deque()

    for s in starts:
        deq.append(s)

    while deq:
        departure = deq.popleft()

        for destination in adj[departure]:
            in_degree[destination] -= 1

            if not in_degree[destination]:
                deq.append(destination)

    if is_cycle(is_exist, in_degree):
        return False

    return True


def can_finish(num_courses, pre_requisites):
    return topology_sort(num_courses, pre_requisites)


print(can_finish(2, [[1, 0]]))
# True
print(can_finish(2, [[1, 0], [0, 1]]))
# False
print(can_finish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
# True
print(can_finish(1, []))
# True
print(can_finish(3, [[1, 0], [2, 0]]))
# True

import copy
import sys
from collections import deque


def bfs(q):
    work_time_original = copy.deepcopy(work_time)

    while q:
        work = q.popleft()

        for next_work in work_schedule[work]:
            work_level[next_work] -= 1
            work_time[next_work] = max(work_time[next_work], work_time[work] + work_time_original[next_work])

            if not work_level[next_work]:
                q.append(next_work)

    return max(work_time)


def topology_sort():
    deq = deque()

    for k in range(1, N + 1):
        if not work_level[k]:
            deq.append(k)

    return bfs(deq)


N = int(sys.stdin.readline())
# 작업 선행 관계
work_schedule = {i: [] for i in range(1, N + 1)}
# 작업 당 시간
work_time = [0] * (N + 1)
# 작업별 진입 차수
work_level = [0] * (N + 1)
for i in range(1, N + 1):
    work_info = list(map(int, sys.stdin.readline().split()))
    work_time[i] = work_info[0]
    prior_works = work_info[1]

    for j in range(2, 2 + prior_works):
        prior_work = work_info[j]
        work_schedule[prior_work].append(i)

    work_level[i] += prior_works

print(topology_sort())

# 반례
# 5
# 6 0
# 3 0
# 3 2 1 2
# 1 1 1
# 1 2 3 4
# => 10

# https://gmlwjd9405.github.io/2018/08/27/algorithm-topological-sort.html
# https://steady-coding.tistory.com/182

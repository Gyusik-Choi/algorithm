import copy
import sys
from collections import deque


def bfs(q):
    answer = copy.deepcopy(building_time)

    while q:
        b = q.popleft()

        for next_b in building_schedule[b]:
            answer[next_b] = max(answer[next_b], answer[b] + building_time[next_b])
            building_level[next_b] -= 1

            if not building_level[next_b]:
                q.append(next_b)

    return answer


def topology_sort():
    deq = deque()

    for k in range(1, N + 1):
        if not building_level[k]:
            deq.append(k)

    return bfs(deq)


N = int(sys.stdin.readline())
building_schedule = {i: [] for i in range(1, N + 1)}
building_time = [0] * (N + 1)
building_level = [0] * (N + 1)
for i in range(1, N + 1):
    buildings = list(map(int, sys.stdin.readline().split()))
    buildings.pop()

    building_time[i] = buildings[0]
    for j in range(1, len(buildings)):
        building = buildings[j]
        building_schedule[building].append(i)
        building_level[i] += 1

max_building_time = topology_sort()
for i in range(1, N + 1):
    sys.stdout.write(str(max_building_time[i]) + "\n")

import sys
from collections import deque


def topology_sort():
    deq = deque()

    for i in range(1, N + 1):
        if not level[i]:
            deq.append(i)

    students_height = []
    while deq:
        level_zero = deq.popleft()
        students_height.append(str(level_zero))

        for student in students[level_zero]:
            level[student] -= 1
            if not level[student]:
                deq.append(student)

    return students_height


N, M = map(int, sys.stdin.readline().split())
students = {i: [] for i in range(1, N + 1)}
level = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    students[A].append(B)
    level[B] += 1

heights = topology_sort()
print(' '.join(heights))

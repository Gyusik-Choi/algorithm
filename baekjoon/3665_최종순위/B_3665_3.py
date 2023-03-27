from collections import deque
import sys


def is_cycle() -> bool:
    for l in range(1, n + 1):
        if level[l]:
            return True

    return False


def topology_sort():
    deq = deque()

    for l in range(1, n + 1):
        if not level[l]:
            deq.append(l)

    answer = []

    while deq:
        start = deq.popleft()
        answer.append(str(start))

        for end in range(1, n + 1):
            if grade[start][end]:
                level[end] -= 1

                if not level[end]:
                    deq.append(end)

    if is_cycle():
        return 'IMPOSSIBLE'

    return ' '.join(answer)


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    last_grades = list(map(int, sys.stdin.readline().split()))

    level = [0] * (n + 1)
    grade = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1):
        high = last_grades[i]

        for j in range(i + 1, n):
            low = last_grades[j]
            level[low] += 1
            grade[high][low] = 1

    m = int(sys.stdin.readline())

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())

        if grade[a][b]:
            grade[a][b] = 0
            level[b] -= 1

            grade[b][a] = 1
            level[a] += 1
        else:
            grade[b][a] = 0
            level[a] -= 1

            grade[a][b] = 1
            level[b] += 1

    sys.stdout.write(topology_sort() + "\n")

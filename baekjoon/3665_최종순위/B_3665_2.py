import sys
from collections import deque


# deq 가 비었고
# degree 는 1 이상인 노드가 있음
def is_cycle():
    for k in range(1, n + 1):
        if degree[k] > 0:
            return True

    return False


def topology_sort():
    deq = deque()

    for k in range(1, n + 1):
        if not degree[k]:
            deq.append(k)

    answer = []

    while deq:
        start = deq.popleft()
        answer.append(str(start))

        for end in range(len(grade[start])):
            # degree[end] 자체 뿐만 아니라
            # start 와 end 관계를 알아야 해서
            # grade[start][end] 조건이 필요
            if grade[start][end]:
                degree[end] -= 1

                if not degree[end]:
                    deq.append(end)

    if is_cycle():
        return 'IMPOSSIBLE'

    return ' '.join(answer)


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    last_year_grade = list(map(int, sys.stdin.readline().split()))

    grade = [[0] * (n + 1) for _ in range(n + 1)]
    degree = [0] * (n + 1)

    for i in range(n - 1):
        front = last_year_grade[i]

        for j in range(i + 1, n):
            back = last_year_grade[j]
            grade[front][back] = 1
            degree[back] += 1

    m = int(sys.stdin.readline())

    for i in range(m):
        front, back = map(int, sys.stdin.readline().split())

        # front 와 back 의
        # 이전 선후 관계를 알지 못해서
        # if grade[front][back] 여부로 판단
        if grade[front][back]:
            grade[front][back] = 0
            degree[back] -= 1

            grade[back][front] = 1
            degree[front] += 1
        else:
            grade[front][back] = 1
            degree[back] += 1

            grade[back][front] = 0
            degree[front] -= 1

    sys.stdout.write(topology_sort() + "\n")

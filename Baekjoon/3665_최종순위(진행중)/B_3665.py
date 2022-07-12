import sys
from collections import deque


def topology_sort():
    deq = deque()
    for i in range(1, n + 1):
        if not level[i]:
            deq.append(i)

    answer = []
    for i in range(1, n + 1):
        if not len(deq):
            return 'IMPOSSIBLE'

        grade = deq.popleft()
        answer.append(str(grade))

        for j in range(1, n + 1):
            if adj_matrix[grade][j]:
                # level[adj_matrix[grade][j]] -= 1
                # if not level[adj_matrix[grade][j]]:
                level[j] -= 1
                if not level[j]:
                    deq.append(j)

    return ' '.join(answer)


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    grades = list(map(int, sys.stdin.readline().split()))

    # adj = {i: [] for i in range(n + 1)} 과 다르게 [] 에 값을 미리 넣었다
    adj_matrix = {i: [0] * (n + 1) for i in range(1, n + 1)}
    level = [0] * (n + 1)
    for i in range(len(grades) - 1):
        for j in range(i + 1, len(grades)):
            adj_matrix[grades[i]][grades[j]] = 1
            level[grades[j]] += 1

    m = int(sys.stdin.readline())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())

        if adj_matrix[a][b]:
            adj_matrix[a][b] = 0
            adj_matrix[b][a] = 1

            # level 값도 바꿔야 함
            level[a] += 1
            level[b] -= 1
        else:
            adj_matrix[a][b] = 1
            adj_matrix[b][a] = 0

            # level 값도 바꿔야 함
            level[a] -= 1
            level[b] += 1

    print(topology_sort())

# 1
# 5
# 5 4 3 2 1
# 2
# 2 4
# 3 4

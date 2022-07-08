import sys


def dfs_recursion(i, visited):
    visited.append(str(i))
    for question in questions[i]:
        if level[question] - 1 == 0 and question not in visited:
            level[question] -= 1
            dfs_recursion(question, visited)

    return visited


def topology_sort():
    visited = []
    for i in range(1, N + 1):
        if not level[i]:
            if i not in visited:
                visited += dfs_recursion(i, [])

    return ' '.join(visited)


N, M = map(int, sys.stdin.readline().split())
questions = {i: [] for i in range(1, N + 1)}
level = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    questions[A].append(B)
    level[B] += 1

for key in questions.keys():
    questions[key].sort()

print(topology_sort())

# 4 2
# 1 4
# 3 2
# => 1 3 2 4

# 5 4
# 4 1
# 5 1
# 2 5
# 3 5
# => ?

# 6 7
# 5 6
# 5 2
# 2 4
# 4 3
# 2 1
# 6 1
# 1 3
# => 5 2 4 6 1 3

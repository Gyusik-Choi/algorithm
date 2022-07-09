# 위상정렬에서 dfs 접근 방식은
# 진입 차수를 활용하는 bfs 와 다르다

import sys


def dfs_recursion():
    pass


def topology_sort():
    pass


N, M = map(int, sys.stdin.readline().split())
questions = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    questions[A].append(B)

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

# https://reakwon.tistory.com/140
# https://sorjfkrh5078.tistory.com/36

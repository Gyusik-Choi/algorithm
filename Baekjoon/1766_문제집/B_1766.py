# 위상정렬에서 dfs 접근 방식은
# 진입 차수를 활용하는 bfs 와 다르다

import sys
import heapq


def bfs(heap):
    answer = []

    while heap:
        question = heapq.heappop(heap)
        answer.append(str(question))

        for q in questions[question]:
            level[q] -= 1
            if level[q] == 0:
                heapq.heappush(heap, q)

    return answer


def topology_sort():
    heap = []
    for i in range(1, N + 1):
        if not level[i]:
            heapq.heappush(heap, i)

    return bfs(heap)


N, M = map(int, sys.stdin.readline().split())
questions = {i: [] for i in range(1, N + 1)}
level = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    questions[A].append(B)
    level[B] += 1

print(' '.join(topology_sort()))

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

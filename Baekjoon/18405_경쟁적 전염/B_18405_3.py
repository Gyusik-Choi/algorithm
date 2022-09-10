import sys
from collections import deque


def bfs(virus_location, q):
    q.sort(key=lambda v: v[1])

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    deq = deque()
    deq.extend(q)

    while deq:
        sec, virus_num, y, x = deq.popleft()

        if sec > S:
            break
        
        if y == Y - 1 and x == X - 1:
            return virus_num

        for k in range(4):
            y_idx = y + y_value[k]
            x_idx = x + x_value[k]

            if 0 <= y_idx < N and 0 <= x_idx < N:
                if not virus_location[y_idx][x_idx]:
                    virus_location[y_idx][x_idx] = virus_num
                    deq.append([sec + 1, virus_num, y_idx, x_idx])

    return 0


# 시험관 길이, 바이러스 번호 최대값
N, K = map(int, sys.stdin.readline().split())
virus_info = []
start_virus = []
for i in range(N):
    virus = list(map(int, sys.stdin.readline().split()))

    for j in range(len(virus)):
        if virus[j] > 0:
            # 초, 번호, 좌표 y, 좌표 x
            start_virus.append([0, virus[j], i, j])
    virus_info.append(virus)

# 초, 좌표 X, 좌표 Y
S, Y, X = map(int, sys.stdin.readline().split())

answer = bfs(virus_info, start_virus)
print(answer)

# 3 2
# 1 0 0
# 0 0 0
# 0 0 2
# 1 2 3
# => 2

# 4 2
# 1 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 2
# 3 3 2
# => 1

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 0 3 2
# => 0

# https://www.acmicpc.net/board/view/85776
# 2 3
# 3 0
# 1 2
# 0 1 1
# => 3

# https://www.acmicpc.net/board/view/58331
# 이 문제에서는 우선순위 큐가 비효율적인 이유에 대한 설명있음

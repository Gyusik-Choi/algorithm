from collections import deque


# 사이클 판별 1
# 진입차수가 0이 아닌 노드가 있는데 deq 가 비워졌다
def is_cycle():
    for i in range(1, v + 1):
        if level[i] > 0:
            return True

    return False


def topology_sort():
    deq = deque()

    for i in range(1, v + 1):
        if level[i] == 0:
            deq.append(i)

    result = []
    while deq:
        s = deq.popleft()

        for node in edges[s]:
            level[node] -= 1
            if level[node] == 0:
                deq.append(node)

        result.append(s)

    if is_cycle():
        return False

    return result


# 정점, 간선 갯수
v, e = map(int, input().split())
edges = {i: [] for i in range(1, v + 1)}
level = [0] * (v + 1)

for _ in range(e):
    start, end = map(int, input().split())
    edges[start].append(end)
    level[end] += 1

answer = topology_sort()
if not answer:
    print("사이클")
else:
    print(answer)

# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# => 1 2 5 3 6 4 7

# 이것이 코딩 테스드다 (나동빈)

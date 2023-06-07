from collections import deque


def is_cycle():
    for l in level:
        if l:
            return True

    return False


def topology_sort():
    answer = []
    deq = deque()

    for idx in range(n):
        if level[idx]:
            continue
        deq.append(idx)

    while deq:
        start = deq.popleft()

        answer.append(start + 1)

        for end in range(n):
            if level[start] < level[end]:
                level[end] -= 1

                if not level[end]:
                    deq.append(end)

    if is_cycle():
        return 'IMPOSSIBLE'

    return answer


t = int(input())
for _ in range(t):
    n = int(input())
    last_year = list(map(int, input().split()))
    m = int(input())

    grade = [[0] * (n + 1) for _ in range(n + 1)]
    level = [0] * (n + 1)
    for i, team in enumerate(last_year):
        level[team] += i

    for _ in range(m):
        a, b = map(int, input().split())
        level[a], level[b] = level[b], level[a]

    print(topology_sort())

# 참고
# https://zoosso.tistory.com/369

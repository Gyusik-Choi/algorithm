from collections import deque


def bfs():
    deq = deque([(S, 0)])
    visited = [False] * (F + 1)
    visited[S] = True

    if S == G:
        return 0

    while deq:
        cur, cnt = deq.popleft()

        for i in range(2):
            current = cur

            if i == 0:
                if current + U > F:
                    continue
                current += U
            else:
                if current - D < 1:
                    continue
                current -= D

            if current == G:
                return cnt + 1

            if not visited[current]:
                visited[current] = True
                deq.append((current, cnt + 1))

    return "use the stairs"


F, S, G, U, D = map(int, input().split())
print(bfs())

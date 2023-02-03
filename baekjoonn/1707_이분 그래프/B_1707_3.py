from collections import deque
import sys


def bfs(start):
    visited[start] = 1

    deq = deque()
    deq.append(start)
    while deq:
        popped_start = deq.popleft()

        for start_number in adj[popped_start]:
            if not visited[start_number]:
                if visited[popped_start] == 1:
                    visited[start_number] = 2
                    deq.append(start_number)
                elif visited[popped_start] == 2:
                    visited[start_number] = 1
                    deq.append(start_number)
            else:
                if visited[start_number] == visited[popped_start]:
                    return False

    return True


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    adj = {i: [] for i in range(1, V + 1)}
    for _ in range(E):
        s, e = map(int, sys.stdin.readline().split())
        adj[s].append(e)
        adj[e].append(s)

    visited = [0] * (V + 1)

    flag = True
    for i in range(1, V + 1):
        if not visited[i]:
            result_bfs = bfs(i)
            if not result_bfs:
                flag = False
                break

    if flag:
        sys.stdout.write("YES" + "\n")
    else:
        sys.stdout.write("NO" + "\n")

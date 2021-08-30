from collections import deque
import sys


def bfs(start, color):
    visited[start - 1] = color

    deq = deque()
    deq.append([start, color])
    while deq:
        popped_start, original_paint_color = deq.popleft()
        paint_color = 1
        if original_paint_color == 1:
            paint_color = 2
        elif original_paint_color == 2:
            paint_color = 1

        for start_number in adj[popped_start]:
            if not visited[start_number - 1]:
                visited[start_number - 1] = paint_color
                deq.append([start_number, paint_color])
            else:
                if visited[start_number - 1] == original_paint_color:
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

    visited = [0] * V
    result_bfs = bfs(1, 1)

    flag = True
    for i in range(len(visited)):
        if not visited[i]:
            result = bfs(i + 1, 1)
            if not result:
                flag = False
                break

    if result_bfs and flag:
        sys.stdout.write("YES" + "\n")
    else:
        sys.stdout.write("NO" + "\n")

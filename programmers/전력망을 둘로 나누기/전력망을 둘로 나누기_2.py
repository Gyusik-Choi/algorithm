from collections import deque


def solution(n, wires):
    def bfs(node):
        cnt = 1
        deq = deque([node])
        visited = [False] * (n + 1)
        visited[node] = True

        while deq:
            start = deq.popleft()

            for end in adj[start]:
                if visited[end]:
                    continue

                visited[end] = True
                deq.append(end)
                cnt += 1

        return cnt

    min_diff = n
    for i, wire in enumerate(wires):
        adj = {i: [] for i in range(1, n + 1)}

        for j, w in enumerate(wires):
            if i == j:
                continue

            v1, v2 = w
            adj[v1].append(v2)
            adj[v2].append(v1)

        min_diff = min(min_diff, abs(bfs(wire[0]) - bfs(wire[1])))

    return min_diff


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))

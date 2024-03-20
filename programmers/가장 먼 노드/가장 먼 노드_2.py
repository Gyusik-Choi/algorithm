from collections import deque


def solution(n, edge):
    def bfs(go):
        visited = [False] * (n + 1)
        visited[go] = True
        inf = float('inf')
        distance = [inf] * (n + 1)
        distance[go] = 0
        deq = deque([[go, 0]])

        while deq:
            start, dist = deq.popleft()
            for end in adj[start]:
                if visited[end]:
                    continue

                visited[end] = True
                distance[end] = dist + 1
                deq.append([end, distance[end]])

        return len(list(filter(lambda x: x == max(distance[1:]), distance[1:])))

    adj = {i: [] for i in range(1, n + 1)}
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)

    return bfs(1)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

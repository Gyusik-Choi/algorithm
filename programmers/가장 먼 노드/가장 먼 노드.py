import heapq


def solution(n, edge):
    def dijkstra(go):
        inf = float('inf')
        visited = [False] * (n + 1)
        distance = [inf] * (n + 1)
        distance[go] = 0
        heap = []
        heapq.heappush(heap, (0, go))

        while heap:
            start_dist, start = heapq.heappop(heap)

            if visited[start]:
                continue

            visited[start] = True
            for end, end_dist in adj[start]:
                if visited[end]:
                    continue

                if distance[end] <= start_dist + end_dist:
                    continue

                distance[end] = start_dist + end_dist
                heapq.heappush(heap, (distance[end], end))

        return len(list(filter(lambda x: x == max(distance[1:]), distance[1:])))

    adj = {i: [] for i in range(1, n + 1)}
    for a, b in edge:
        adj[a].append([b, 1])
        adj[b].append([a, 1])

    return dijkstra(1)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

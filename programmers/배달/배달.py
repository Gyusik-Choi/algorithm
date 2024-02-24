import heapq


def solution(n, road, k):
    def dijkstra(maps, start):
        distances = [float('inf')] * (n + 1)
        distances[start] = 0
        visited = [False] * (n + 1)
        heap = [(distances[start], start)]

        while heap:
            s_dist, s = heapq.heappop(heap)

            if visited[s]:
                continue

            visited[s] = True

            for e, e_dist in maps[s]:
                if visited[e]:
                    continue

                if distances[e] < s_dist + e_dist:
                    continue

                distances[e] = s_dist + e_dist
                heapq.heappush(heap, (distances[e], e))

        return distances

    adj = {i: [] for i in range(1, n + 1)}
    for r in road:
        a, b, c = r
        adj[a].append([b, c])
        adj[b].append([a, c])

    # 1번 마을도 포함
    return len(list(filter(lambda x: 0 < x <= k, dijkstra(adj, 1)))) + 1


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))

import heapq


def find_answer(distance):
    max_dist = max(distance)
    # https://bobbyhadz.com/blog/python-join-integer-list
    return " ".join(map(str, [distance.index(max_dist) + 1, max_dist, distance.count(max_dist)]))



def dijkstra(n, go, barn):
    inf = float('inf')
    distance = [inf] * (n + 1)
    visited = [False] * (n + 1)

    heap = []
    distance[go] = 0
    heapq.heappush(heap, (0, go))

    while heap:
        start_dist, start_idx = heapq.heappop(heap)

        if visited[start_idx]:
            continue

        visited[start_idx] = True

        for end_dist, end_idx in barn[start_idx]:
            if visited[end_idx]:
                continue

            if start_dist + end_dist > distance[end_idx]:
                continue

            distance[end_idx] = start_dist + end_dist
            heapq.heappush(heap, (distance[end_idx], end_idx))

    distance.pop(0)
    return find_answer(distance)


N, M = map(int, input().split())
barns = {i: [] for i in range(N + 1)}

for _ in range(M):
    A, B = map(int, input().split())
    barns[A].append([1, B])
    barns[B].append([1, A])

print(dijkstra(N, 1, barns))

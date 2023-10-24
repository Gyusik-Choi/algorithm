import heapq


# 1 ~ n
def dijkstra(node, n, go):
    inf = float('inf')
    visited = [False] * (n + 1)
    distances = [inf] * (n + 1)
    # distances 에서 max 함수를 쓸 때
    # 0 인덱스가 inf 로 남아 있어서
    # 이를 막기 위해 0 으로 변경
    distances[0] = 0
    distances[go] = 0
    # 거리, 번호
    heap = [[0, go]]

    while heap:
        start_dist, start = heapq.heappop(heap)

        if visited[start]:
            continue

        visited[start] = True

        if start not in node:
            continue

        for end, end_dist in node[start]:
            if visited[end]:
                continue

            if distances[end] > start_dist + end_dist:
                distances[end] = start_dist + end_dist
                heapq.heappush(heap, [distances[end], end])

    if max(distances) == inf:
        return -1

    return max(distances)


def network_delay_time(times, n, k):
    nodes = dict()

    for source, target, time in times:
        if source in nodes:
            nodes[source].append([target, time])
        else:
            nodes[source] = [[target, time]]

    return dijkstra(n, k, nodes)


print(network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(network_delay_time([[1, 2, 1]], 2, 1))
print(network_delay_time([[1, 2, 1]], 2, 2))

from collections import defaultdict
import heapq


def network_delay_time(times, n, k):
    graph = defaultdict(list)

    for u, v, w in times:
        graph[u].append([v, w])

    heap = [[0, k]]
    distance = dict()

    while heap:
        start_time, start = heapq.heappop(heap)

        if start not in distance:
            distance[start] = start_time

            for end, end_time in graph[start]:
                # 해당 end 가 heapq 에서
                # 언젠가 나왔을 때
                # 위의 if start not in distance 에
                # 걸리긴 하는데
                # heap 에 아예 넣지 않기 위해
                # 여기서도 if 문으로 검사한다
                if end not in distance:
                    heapq.heappush(heap, [start_time + end_time, end])

    if len(distance) == n:
        return max(distance.values())

    return -1


print(network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(network_delay_time([[1, 2, 1]], 2, 1))
print(network_delay_time([[1, 2, 1]], 2, 2))

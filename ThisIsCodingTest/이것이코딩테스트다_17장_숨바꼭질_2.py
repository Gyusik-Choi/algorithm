import sys
import heapq


def find_answer(distances):
    max_barn_number = 0
    max_barn_distance = max(distances)
    max_barn_cnt = 0

    for number in range(len(distances) - 1, 0, -1):
        distance = distances[number]
        if max_barn_distance == distance:
            max_barn_number = number
            max_barn_distance = distance
            max_barn_cnt += 1

    return ' '.join([str(max_barn_number), str(max_barn_distance), str(max_barn_cnt)])


def dijkstra():
    selected = [False] * (N + 1)
    distances = [float('inf')] * (N + 1)
    # 최대 거리 구할때 max 에 걸리지 않도록
    # 없는 번호인 0도 값을 0으로 만든다
    distances[0] = 0
    distances[1] = 0
    heap = []
    # 거리, 번호
    heapq.heappush(heap, (0, 1))

    while heap:
        start_dist, start_num = heapq.heappop(heap)

        if selected[start_num]:
            continue

        selected[start_num] = True
        for end_dist, end_num in maps[start_num]:
            if not selected[end_num]:
                if distances[end_num] > start_dist + end_dist:
                    distances[end_num] = start_dist + end_dist
                    heapq.heappush(heap, (distances[end_num], end_num))

    return find_answer(distances)


N, M = map(int, sys.stdin.readline().split())
maps = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    maps[A].append([1, B])
    maps[B].append([1, A])

print(dijkstra())

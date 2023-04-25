import sys
import heapq


def find_numbers_by_distance(distances, target_distance):
    answer = ''

    for i, distance in enumerate(distances):
        if distance != target_distance:
            continue

        answer += str(i) + "\n"

    if not answer:
        return str(-1)

    return answer.rstrip("\n")


def dijkstra(start, target_distance):
    inf = float('inf')
    distance = [inf] * (N + 1)
    selected = [False] * (N + 1)

    distance[start] = 0
    heap = []
    # 거리, 번호
    heapq.heappush(heap, [distance[start], start])

    while heap:
        departure_dist, departure = heapq.heappop(heap)

        if selected[departure]:
            continue

        selected[departure] = True

        for destination, destination_dist in cities[departure]:
            if selected[destination]:
                continue

            if departure_dist + destination_dist < distance[destination]:
                distance[destination] = departure_dist + destination_dist
                heapq.heappush(heap, [distance[destination], destination])

    return find_numbers_by_distance(distance, target_distance)


N, M, K, X = map(int, sys.stdin.readline().split())
cities = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    cities[A].append([B, 1])

sys.stdout.write(dijkstra(X, K))

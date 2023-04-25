import sys


class MinHeap:
    def __init__(self):
        self.heap = [[None]]

    def heappush(self, num):
        self.heap.append(num)

        child = len(self.heap) - 1

        while child > 1:
            parent = child // 2

            if self.heap[parent] > self.heap[child]:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                child //= 2
            else:
                break

    def heappop(self) -> list:
        if len(self.heap) <= 1:
            return []

        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]

        num = self.heap.pop()

        self.__heapify(1)

        return num

    def __heapify(self, idx):
        parent_idx = idx
        left_child_idx = parent_idx * 2
        right_child_idx = parent_idx * 2 + 1

        if left_child_idx < len(self.heap) and self.heap[parent_idx] > self.heap[left_child_idx]:
            parent_idx = left_child_idx

        if right_child_idx < len(self.heap) and self.heap[parent_idx] > self.heap[right_child_idx]:
            parent_idx = right_child_idx

        if parent_idx != idx:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            return self.__heapify(parent_idx)


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
    min_heap = MinHeap()
    # 거리, 번호
    min_heap.heappush([distance[start], start])

    while len(min_heap.heap) > 1:
        departure_dist, departure = min_heap.heappop()

        if selected[departure]:
            continue

        selected[departure] = True

        for destination, destination_dist in cities[departure]:
            if selected[destination]:
                continue

            if departure_dist + destination_dist < distance[destination]:
                distance[destination] = departure_dist + destination_dist
                min_heap.heappush([distance[destination], destination])

    return find_numbers_by_distance(distance, target_distance)


N, M, K, X = map(int, sys.stdin.readline().split())
cities = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    cities[A].append([B, 1])

sys.stdout.write(dijkstra(X, K))

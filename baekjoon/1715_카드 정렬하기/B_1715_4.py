import heapq
import sys


def get_sums(h):
    total_sums = 0

    while len(h) > 1:
        num1 = heapq.heappop(h)
        num2 = heapq.heappop(h)

        sums = num1 + num2
        total_sums += sums
        heapq.heappush(h, sums)

    return total_sums


N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

print(get_sums(heap))

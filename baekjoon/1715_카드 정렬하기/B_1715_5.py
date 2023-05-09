import heapq
import sys


N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

sums = 0

while len(heap) > 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)

    sums += num1 + num2
    heapq.heappush(heap, num1 + num2)

print(sums)

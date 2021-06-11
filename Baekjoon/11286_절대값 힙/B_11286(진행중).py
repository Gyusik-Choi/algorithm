import heapq
import sys

N = int(input())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        absolute_num, number = heapq.heappop(heap)
        sys.stdout.write(str(number))
    else:
        abs_num = abs(num)
        heapq.heappush(heap, (abs_num, num))

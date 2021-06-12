import heapq
import sys

N = int(input())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if not heap:
            sys.stdout.write(str(0) + "\n")
        else:
            absolute_num, number = heapq.heappop(heap)
            sys.stdout.write(str(number) + "\n")
    else:
        abs_num = abs(num)
        heapq.heappush(heap, (abs_num, num))

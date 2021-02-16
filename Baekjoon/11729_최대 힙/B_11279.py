import heapq
import sys


N = int(input())
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    if not heap:
        if num == 0:
            sys.stdout.write('0' + '\n')
        else:
            heapq.heappush(heap, (-num, num))
    else:
        if num == 0:
            max_num = heapq.heappop(heap)
            sys.stdout.write(str(max_num[1]) + '\n')
        else:
            heapq.heappush(heap, (-num, num))

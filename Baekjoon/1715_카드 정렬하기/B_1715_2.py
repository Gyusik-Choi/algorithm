import sys
import heapq


N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    heapq.heappush(heap, n)

answer = 0

while len(heap) > 1:
    temp_sums = heapq.heappop(heap)
    temp_sums += heapq.heappop(heap)
    answer += temp_sums
    heapq.heappush(heap, temp_sums)


print(answer)

# 20 40 100 120
# 60 160 280

# 20 40 (100 120)
# 60 100 (120)
# 120 160

# https://www.acmicpc.net/board/view/72799

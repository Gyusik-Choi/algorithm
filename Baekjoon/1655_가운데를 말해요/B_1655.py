import heapq
import sys


N = int(input())
left_heap = []
right_heap = []

for _ in range(N):
    number = int(sys.stdin.readline().rstrip())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-number, number))
    else:
        heapq.heappush(right_heap, (number, number))

    if right_heap and left_heap[0][1] > right_heap[0][1]:
        left_pop = heapq.heappop(left_heap)
        right_pop = heapq.heappop(right_heap)

        left_pop_item = left_pop[1]
        right_pop_item = right_pop[1]

        heapq.heappush(left_heap, (-right_pop_item, right_pop_item))
        heapq.heappush(right_heap, (left_pop_item, left_pop_item))

    ans = left_heap[0][1]
    sys.stdout.write(str(ans) + "\n")

# 참고
# https://www.acmicpc.net/source/29917071
# https://inspirit941.tistory.com/200
# https://deok2kim.tistory.com/227

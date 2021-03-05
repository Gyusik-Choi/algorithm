import heapq
import sys


N = int(input())
nums = []
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if not nums:
            sys.stdout.write(str(0) + '\n')
        else:
            min_num = heapq.heappop(nums)
            sys.stdout.write(str(min_num) + '\n')
    else:
        heapq.heappush(nums, num)

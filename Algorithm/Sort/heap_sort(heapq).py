import heapq

heap = []

arr = [5, 2, 1, 3, 4]
for a in arr:
    heapq.heappush(heap, a)

sorted_arr = []
while heap:
    num = heapq.heappop(heap)
    sorted_arr.append(num)

print(sorted_arr)

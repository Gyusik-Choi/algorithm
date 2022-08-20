import heapq


def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    heap = []
    for food_idx, food_time in enumerate(food_times):
        heapq.heappush(heap, (food_time, food_idx + 1))

    food_length = len(food_times)
    previous_time = 0

    while k - ((heap[0][0] - previous_time) * food_length) > 0:
        time, idx = heapq.heappop(heap)
        k -= (time - previous_time) * food_length
        food_length -= 1
        previous_time = time

    heap.sort(key=lambda x: x[1])
    return heap[k % food_length][1]


print(solution([3, 1, 2], 5))
print(solution([2, 3, 1, 5, 4], 3))

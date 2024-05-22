import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = []
    for i, v in enumerate(food_times):
        heapq.heappush(heap, (v, i + 1))

    food_length = len(food_times)
    previous_time = 0

    while k - ((heap[0][0] - previous_time) * food_length) > 0:
        now_time, now_idx = heapq.heappop(heap)
        k -= (now_time - previous_time) * food_length
        food_length -= 1
        previous_time = now_time

    sorted_heap = sorted(heap, key=lambda x: x[1])
    return sorted_heap[k % food_length][1]


print(solution([3, 1, 2], 5))
print(solution([2, 3, 1, 5, 4], 3))

import heapq
from collections import Counter


def top_k_frequent(nums, k):
    num_cnt = Counter(nums)
    heap = []

    for key, value in num_cnt.items():
        heapq.heappush(heap, (-value, key))

    answer = []

    for _ in range(k):
        answer.append(heapq.heappop(heap)[1])

    return answer


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent([1], 1))

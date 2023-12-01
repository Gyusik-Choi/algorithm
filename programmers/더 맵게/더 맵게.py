import heapq


def solution(scoville, k):
    heap = []

    for s in scoville:
        heapq.heappush(heap, s)

    cnt = 0

    while len(heap) >= 2:
        first_scoville = heapq.heappop(heap)
        second_scoville = heapq.heappop(heap)

        if first_scoville >= k:
            break

        heapq.heappush(heap, first_scoville + (second_scoville * 2))
        cnt += 1

    # 힙에 요소가 남아있는 경우
    if heap and heap[0] < k:
        return -1

    return cnt


print(solution([1, 2, 3, 9, 10, 12], 7))

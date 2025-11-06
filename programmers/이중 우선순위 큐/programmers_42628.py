import heapq
from collections import defaultdict


def solution(operations):
    def is_empty():
        return len(min_heap) == 0 or len(max_heap) == 0

    def remove_invalid_min_heap_element():
        while len(min_heap) > 0 and history[min_heap[0]] == 0:
            heapq.heappop(min_heap)

    def remove_invalid_max_heap_element():
        while len(max_heap) > 0 and history[max_heap[0] * -1] == 0:
            heapq.heappop(max_heap)

    min_heap = []
    max_heap = []
    history = defaultdict(int)
    for operation in operations:
        command, data = operation.split(' ')
        data = int(data)

        if command == 'I':
            history[data] += 1
            heapq.heappush(min_heap, data)
            heapq.heappush(max_heap, data * -1)
        else:
            if data < 0:
                remove_invalid_min_heap_element()
                if len(min_heap) == 0:
                    continue
                min_num = heapq.heappop(min_heap)
                history[min_num] -= 1
            else:
                remove_invalid_max_heap_element()
                if len(max_heap) == 0:
                    continue
                max_num = heapq.heappop(max_heap)
                max_num *= -1
                history[max_num] -= 1

    remove_invalid_min_heap_element()
    remove_invalid_max_heap_element()
    return [0, 0] if is_empty() else [heapq.heappop(max_heap) * -1, heapq.heappop(min_heap)]

# 참고
# https://school.programmers.co.kr/questions/64721

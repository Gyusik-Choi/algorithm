from unittest import TestCase
import heapq


def heap_sort(arr):
    heap = []
    for idx, num in enumerate(arr):
        heapq.heappush(heap, num)

    sorted_arr = []
    while heap:
        num = heapq.heappop(heap)
        sorted_arr.append(num)

    return sorted_arr


class HeapSortTest(TestCase):
    def test_heap_sort(self):
        arr = [5, 4, 3, 2, 1]
        answer = heap_sort(arr)
        self.assertEqual(answer, sorted(arr))
